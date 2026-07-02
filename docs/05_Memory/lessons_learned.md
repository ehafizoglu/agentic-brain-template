---
project: "PROJECT_NAME"
role: "Memory"
last_updated: 2026-07-02
tags:
  - memory
  - lessons
  - optimization
---

# 🧠 Brain Vault: Lessons Learned & Engineering Memory

◀️ Back to [[Project_Hub]]

This file contains the collective memory of what worked, what failed, and the solutions to tricky bugs or performance bottlenecks discovered during this project. Read this file before initiating refactoring.

---

## 🪱 Quirks & Gotchas (Neleri Fark Ettik?)
*Track platform, API, or package behavior that was unexpected.*

1. **PowerShell `Get-Content` UTF-8 Encoding**:
   - *Problem*: Emojis got corrupted to ANSI sequences like `ğŸ•µï¸` during compilation.
   - *Cause*: Standard Windows PowerShell (v5.1) reads file contents as ANSI by default if `-Encoding` is not specified.
   - *Solution*: Always specify `-Encoding utf8` when using `Get-Content` or `Out-File` cmdlets in PowerShell.

---

## 🐛 Resolved Bug Log (Çözülen Hatalar)
*A log of hard-to-find bugs and their resolutions.*

### 🐞 [BUG-001] JWT Cookie Expiry Mismatch
- **Symptoms**: Users get logged out randomly after 15 minutes, even though session cookie lifetime is set to 7 days.
- **Root Cause**: The JWT token inside the cookie has an internal `exp` claim set to 15m (default configuration), which overrides the browser cookie's expiration.
- **Fix**: Updated JWT signing logic to pass `{ expiresIn: '7d' }` matching the cookie configuration.

---

## 💡 Best Practices & Performance Wins (Optimizasyonlar)
*Record code structures that improved efficiency.*

- **Modular Context Feeding**: Only supply the target AI with files relevant to its task (e.g., just `business_requirements.md` when designing a feature) to preserve system context windows and save token cost.
