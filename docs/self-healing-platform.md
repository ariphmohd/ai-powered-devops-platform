# ♻️ Container Health Checks & Self-Healing

## Overview

The platform implements container health monitoring to ensure application reliability and automatic recovery.

Docker health checks continuously validate application availability using the `/health` endpoint.

---

## Health Check Mechanism

Docker periodically executes:

```
http://localhost:8000/health
```

Configuration:

```
HEALTHCHECK --interval=30s --timeout=5s --retries=3
```

If the health endpoint fails repeatedly, Docker marks the container as unhealthy.

---

## Automatic Recovery

Containers use:

```
restart: always
```

This enables automatic restart when failures occur.

---

## Failure Simulation

Example test:

```
docker exec -it app bash
pkill -f uvicorn
```

Docker automatically restores the service.

---

## Reliability Benefits

* Automatic failure detection
* Reduced downtime
* Self-healing behavior
* Production-ready resilience model

---

## SRE Concept Demonstrated

This implementation reflects core Site Reliability Engineering practices:

* Health probing
* Failure detection
* Automated recovery
* Service reliability assurance

