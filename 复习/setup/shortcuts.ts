import type { NavOperations, ShortcutOptions } from '@slidev/types'
import { defineShortcutsSetup } from '@slidev/types'

export default defineShortcutsSetup((nav: NavOperations, base: ShortcutOptions[]) => {
  return base.map((shortcut) => {
    if (shortcut.name === 'next_down' || shortcut.name === 'next_shift') {
      return { ...shortcut, fn: () => nav.next(), autoRepeat: true }
    }
    if (shortcut.name === 'prev_up' || shortcut.name === 'prev_shift') {
      return { ...shortcut, fn: () => nav.prev(), autoRepeat: true }
    }
    return shortcut
  })
})
