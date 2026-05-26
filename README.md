# MCP Registry Management Skill

> MCP control plane — register servers, discover tools, manage allow-lists, monitor health, restart unhealthy servers, and export inventory for the enterprise MCP fleet.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | Achieves |
|----------|-------|----------|
| Discover | 1-2 | List servers + available tools |
| Register | 2 | Validate manifest → register |
| Health Monitor | 1-2 | Check + restart if unhealthy |
| Allow-List | 1 | Grant/revoke tool access |

### Without this skill:
- No visibility into which MCP servers are available
- Unhealthy servers go undetected
- No access control (all tools available to all agents)

### With this skill:
- Full fleet visibility with health status
- Unhealthy servers detected and auto-restarted
- Allow-lists enforced (explicit access only)
- Manifest validation before registration

## Installation

```bash
git clone https://github.com/zavora-ai/skill-mcp-registry-management.git \
  ~/.skills/skills/mcp-registry-management
```

## Requirements

**Required:** `mcp-registry` (10 tools)
**Cross-MCP:** mcp-credentials-vault (server auth), mcp-slack (health alerts)

## Example

**User:** "Are all MCP servers healthy?"

**Result:**
```
Fleet Health: 12/13 servers healthy (92.3%)
⚠️ Unhealthy: mcp-crm — connection timeout
Action: Auto-restart triggered. Will re-check in 60s.
```

## Scripts

### `health_report.py`
```bash
python scripts/health_report.py '[{"name": "mcp-crm", "status": "unhealthy"}, {"name": "mcp-email", "status": "healthy"}]'
# → {"total": 2, "healthy": 1, "unhealthy": 1, "health_pct": 50.0}
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)

## Success Criteria

| Metric | Target |
|--------|--------|
| Trigger rate | 90% on relevant queries |
| Compliance | 100% governed actions evaluated |
| Audit trail | Every action logged with actor + reason |

## Related Skills

See the full [ADK-Rust Enterprise Skills Registry](https://github.com/zavora-ai) for all 35 skills.

