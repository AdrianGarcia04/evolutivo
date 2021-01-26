import plot
from Particle import *

def pso(fnct, blo, bup, maxevals, size, dim, omega, phip, phig, lr, gif, data, log, nBest):
    (swarm, swarmBest) = createSwarm(size, dim, blo, bup, fnct)
    eval = 0
    while eval < maxevals:
        print(f'Eval: {eval} - {maxevals}', end='\r')
        for particle in swarm:
            newVelocity = np.zeros(shape=dim)
            for d in range(dim):
                rp = np.random.uniform()
                rg = np.random.uniform()

                currentPosD = particle.position[d]
                currentVelD = particle.velocities[d]
                bestPosD = particle.personalBest[d]

                diffP = bestPosD - currentPosD
                diffB = swarmBest[d] - currentPosD
                newVelocity[d] = omega * currentVelD + (phip * rp * (diffP)) + (phig * rg * (diffP))


            particle.velocities = newVelocity
            particle.position = particle.position + lr * particle.velocities

            fitnessVal = particle.fitness(fnct)
            bestFitnessVal = particle.bestFitness(fnct)

            if fitnessVal < bestFitnessVal:
                particle.personalBest = particle.position

                if bestFitnessVal < fnct(swarmBest[0], swarmBest[1]):
                    swarmBest = particle.personalBest
        eval += 1
        if data:
            sorted = sortByFitness(swarm)
            nBestList = sorted[-nBest:]
            avgFitness = np.average(nBestList)

            for b in range(nBest):
                log.add_data(f'iter-best{b}', (eval, nBestList[b]))

            log.add_data('iter-avg', (eval, avgFitness))

        if gif:
            plot.savefig(eval, blo, bup, fnct, swarm)

def sortByFitness(swarm):
    sorted = [p.fitnessVal for p in swarm]
    sorted.sort()
    return sorted
