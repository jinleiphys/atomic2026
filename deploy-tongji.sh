#!/bin/bash
# 同步 atomic_slide 到 tongji 服务器 (192.168.50.11:8888)
# 用法: ./deploy-tongji.sh [--build]
#   --build  先构建第二章slidev再部署（默认跳过构建，只同步文件）

set -e

REMOTE="tongji"
REMOTE_DIR="/var/www/html/atomic2026"
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}=== atomic_slide 部署到 tongji ===${NC}"
echo "项目目录: $PROJECT_DIR"
echo "远程目录: $REMOTE:$REMOTE_DIR"
echo ""

# Step 0: 检查SSH连接
echo -e "${YELLOW}[0/4] 检查SSH连接...${NC}"
if ! ssh -o ConnectTimeout=5 $REMOTE "echo ok" > /dev/null 2>&1; then
    echo "错误: 无法连接到 $REMOTE，请检查VPN或网络"
    exit 1
fi
echo "  连接正常"

# Step 1: 构建第二章 (可选)
if [[ "$1" == "--build" ]]; then
    echo -e "${YELLOW}[1/4] 构建第二章 Slidev...${NC}"
    cd "$PROJECT_DIR/第二章"
    npx slidev build --base /ch2/dist/
    echo "  构建完成"
    cd "$PROJECT_DIR"
else
    echo -e "${YELLOW}[1/4] 跳过构建（使用 --build 参数来构建第二章）${NC}"
fi

# Step 2: 同步静态文件
echo -e "${YELLOW}[2/4] 同步静态文件...${NC}"

# 首页
echo "  - index.html"
rsync -az "$PROJECT_DIR/index.html" $REMOTE:$REMOTE_DIR/

# 第一章
echo "  - 第一章/"
rsync -az "$PROJECT_DIR/第一章/" $REMOTE:$REMOTE_DIR/第一章/

# AI Workshop
echo "  - AI-workshop/"
rsync -az "$PROJECT_DIR/AI-workshop/" $REMOTE:$REMOTE_DIR/AI-workshop/

# Step 3: 同步第二章构建产物
echo -e "${YELLOW}[3/4] 同步第二章 dist...${NC}"
if [ -d "$PROJECT_DIR/第二章/dist" ]; then
    # 用tar打包避免中文路径问题
    tar czf /tmp/slidev-dist.tar.gz -C "$PROJECT_DIR/第二章/dist" .
    scp -q /tmp/slidev-dist.tar.gz $REMOTE:/tmp/
    ssh $REMOTE "mkdir -p $REMOTE_DIR/ch2/dist && \
                 rm -rf $REMOTE_DIR/ch2/dist/* && \
                 cd $REMOTE_DIR/ch2/dist && \
                 tar xzf /tmp/slidev-dist.tar.gz && \
                 rm /tmp/slidev-dist.tar.gz"
    rm /tmp/slidev-dist.tar.gz
    echo "  上传完成"
else
    echo "  警告: 第二章/dist 不存在，跳过（使用 --build 参数先构建）"
fi

# Step 4: 确保SPA HTTP服务运行
echo -e "${YELLOW}[4/4] 检查HTTP服务...${NC}"

# 上传SPA服务脚本
cat << 'PYSERVE' | ssh $REMOTE "cat > $REMOTE_DIR/serve.py"
#!/usr/bin/env python3
"""SPA-aware HTTP server for atomic2026"""
import http.server
import os

ROOT = '/var/www/html/atomic2026'
PORT = 8888

class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        # For SPA routes under /ch2/dist/, serve index.html if file not found
        path = self.translate_path(self.path)
        if not os.path.exists(path) and self.path.startswith('/ch2/dist/'):
            self.path = '/ch2/dist/index.html'
        super().do_GET()

if __name__ == '__main__':
    with http.server.HTTPServer(('0.0.0.0', PORT), SPAHandler) as httpd:
        print(f'Serving on port {PORT} with SPA fallback...')
        httpd.serve_forever()
PYSERVE

# 重启服务
ssh $REMOTE << 'RESTART'
kill $(pgrep -f "http.server\|serve.py") 2>/dev/null || true
sleep 1
cd /var/www/html/atomic2026
nohup python3 serve.py </dev/null >/tmp/serve.log 2>&1 &
sleep 1
echo "pid: $(pgrep -f serve.py)"
RESTART

if ssh $REMOTE "curl -s -o /dev/null -w '%{http_code}' http://localhost:8888/ch2/dist/1" 2>/dev/null | grep -q "200"; then
    echo "  SPA HTTP服务正常运行 (port 8888)"
else
    echo "  警告: 服务可能未正常启动，请检查 ssh tongji 'cat /tmp/serve.log'"
fi

echo ""
echo -e "${GREEN}=== 部署完成 ===${NC}"
echo "访问: http://192.168.50.11:8888/"
echo "第二章: http://192.168.50.11:8888/ch2/dist/"
echo "AI Workshop: http://192.168.50.11:8888/AI-workshop/"
