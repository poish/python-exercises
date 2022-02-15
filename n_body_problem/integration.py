def RK4(system, body, dt):

    projected = body.copy()
    dV1 = system.force(projected)
    dP1 = body.vel * dt

    # projected.reset() not neccessary

    projected.project(dP1 / 2, dV1 / 2)
    dV2 = system.force(projected)
    dP2 = (body.vel + dV1 / 2)*dt

    projected.reset()

    projected.project(dP2 / 2, dV1 / 2)
    dV3 = system.force(projected)
    dP3 = (body.vel + dV2 / 2)*dt

    projected.reset()

    projected.project(dP3, dV1)
    dV4 = system.force(projected)
    dP4 = (body.vel + dV3 / 2)*dt

    dP = (dP1 + dP2 * 2 + dP3 * 3 + dP4)/6
    dV = (dV1 + dV2 * 2 + dV3 * 3 + dV4)/6

    body.pos += dP
    body.vel += dV