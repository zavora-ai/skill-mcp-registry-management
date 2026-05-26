# MCP Registry Cross-MCP Workflows

## Registry + Credentials: Server Onboarding
```
REGISTRY: register_server(manifest: {..., credentials: ["vault://new-token"]})
CREDENTIALS: validate_secret_scope(secret: "new-token") → valid
REGISTRY: health_check(server_id: "new_server") → healthy
REGISTRY: allow_list_tools(server_id, tools: ["tool_1", "tool_2"], agents: ["agent_1"])
```

## Registry + Slack: Health Alerts
```
REGISTRY: health_check(server_id: "mcp_crm") → {status: "unhealthy", error: "connection_timeout"}
SLACK: send_message(channel: "#platform", text: "⚠️ mcp_crm unhealthy: connection timeout. Auto-restart in 60s.")
REGISTRY: restart_server(server_id: "mcp_crm")
```
