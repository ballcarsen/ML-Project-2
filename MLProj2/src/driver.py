#!/usr/bin/env python3

"""
arg0: Invoking script
arg1: # of parameters for the rosenbrock function
arg2: # of MLP hidden layers
arg3: # of MLP hidden neurons
arg4: # of MLP output neurons
arg5: # of RBF hidden neurons
arg6: # of RBF output neurons
arg7: # of data points
"""

from experiment import Tester
from experiment.generate_data import GenerateData as GD
from backprop.bpAlg import BPAlg as BP
from radialBasis.radialBasisOut import radialBasisOut as RFB
import sys


if __name__ == "__main__":
    
    try:
        train = GD(int(sys.argv[7]), int(sys.argv[1]), int(sys.argv[4]))
        train.simple_random_sample(-1, 1)
        train_data = train.get_data()
        train_target = train.get_target_vector()
            
        bp = BP()
        bp_network = bp.train(train_data, train_target, int(sys.argv[2]), int(sys.argv[3]))

        rfb = RFB(train_data, train_target, int(sys.argv[5]), int(sys.argv[6]), 0.05)

        #test = GD(int(sys.argv[7]), int(sys.argv[1]))
        #test_data = test.get_data()
        #test_target = test.get_target_vector()
    
        # t = Tester(bp.test(test_data, test_target, bp_network), rfb.test(test_data, test_target), "bp", "rbf")
        # t.compare()

        pass
    except IndexError:
        print("Not enough arguments provided.")
    finally:
        sys.exit()









