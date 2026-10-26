# AI agents and orchestration platforms

The catalog includes six projects requested for the Linux software list. They have **different roles**: personal agents, coding agents, orchestration and collaboration. These are discovery entries, not benchmarks or endorsements; none was locally installed or security-audited for this catalog.

| Project | Primary role | Upstream repository |
| --- | --- | --- |
| OpenClaw | Personal assistant and tool automation | [openclaw/openclaw](https://github.com/openclaw/openclaw) |
| Hermes Agent | Personal agent with persistent memory and skills | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) |
| Agent Zero | General-purpose autonomous agent framework | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) |
| OpenHands | AI coding agent and development control center | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) |
| Paperclip | Multi-agent orchestration, tasks and governance | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) |
| Buzz (Block) | Communication and shared workspaces for humans and agents | [block/buzz](https://github.com/block/buzz) |

The [generated software index](../../generated/software-index.md) provides searchable links, while [YAML source records](../../data/software/) retain evidence and classification.

## Linux deployment considerations

Check each upstream project's current Linux prerequisites, container/runtime dependencies, access controls, model-provider requirements, and resource consumption before installing. Listing here does not establish native Debian availability or local-LLM compatibility.

For agents capable of running commands, editing files or using external services, prefer isolated test environments, restricted credentials, private network access and approval gates. Never grant unrestricted host access or production API keys without reviewing the project's security model.
