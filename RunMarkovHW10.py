import InputDataHW10 as Data
import Scratch as SupportMarkov
import Scratch4 as P
import Scratch3 as MarkovCls


print("Problem 1")
print(P.calculate_prob_matrix())
print(P.calculate_prob_matrix_anticoag())
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)

simOutputs = cohort.simulate()


cohort2 = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)

simOutputs2 = cohort2.simulate()

SupportMarkov.print_outcomes(simOutputs, 'No treatment:')
SupportMarkov.print_outcomes(simOutputs2, 'Anticoagulation treatment:')

print("Problem 2")
SupportMarkov.print_comparative_outcomes(simOutputs, simOutputs2)

print("Problem 3")
SupportMarkov.report_CEA_CBA(simOutputs, simOutputs2)

print("Problem 4")
print("I would be willing to pay for this at around $20,280 per QALY")

print("Thanks Reza for your help")
