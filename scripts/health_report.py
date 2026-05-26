#!/usr/bin/env python3
"""Generate health report from server status data."""
import json, sys

def report(servers):
    healthy = [s for s in servers if s.get("status") == "healthy"]
    unhealthy = [s for s in servers if s.get("status") != "healthy"]
    return {
        "total": len(servers),
        "healthy": len(healthy),
        "unhealthy": len(unhealthy),
        "health_pct": round(len(healthy) / len(servers) * 100, 1) if servers else 0,
        "action_needed": [{"server": s["name"], "status": s["status"], "error": s.get("error", "")} for s in unhealthy],
    }

if __name__ == "__main__":
    print(json.dumps(report(json.loads(sys.argv[1])), indent=2))
