#    This file is part of EAP.
#
#    EAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    EAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with EAP. If not, see <http://www.gnu.org/licenses/>.

import array
import sys
import random
import logging

sys.path.append("..")

import eap.algorithms as algorithms
import eap.base as base
import eap.creator as creator
import eap.halloffame as halloffame
import eap.toolbox as toolbox

logging.basicConfig(level=logging.DEBUG)
random.seed(64)

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", array.array, fitness=creator.FitnessMax)

tools = toolbox.Toolbox()

# Attribute generator
tools.register("attr_bool", random.randint, 0, 1)

# Structure initializers
tools.regInit("individual", creator.Individual, content=tools.attr_bool, size=100, args=("b",))
tools.regInit("population", list, content=tools.individual, size=300)

def evalOneMax(individual):
    return sum(individual),

tools.register("evaluate", evalOneMax)
tools.register("mate", toolbox.cxTwoPoints)
tools.register("mutate", toolbox.mutFlipBit, indpb=0.05)
tools.register("select", toolbox.selTournament, tournsize=3)

hof = halloffame.HallOfFame(1)

pop = tools.population()
algorithms.eaSimple(tools, pop, cxpb=0.5, mutpb=0.2, ngen=40, halloffame=hof)

logging.info("Best individual is %r, %r", hof[0], hof[0].fitness.values)