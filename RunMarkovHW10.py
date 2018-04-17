import InputDataHW10 as Data
import Support as SupportMarkov
import Parameters as P
import MarkovClasses as MarkovCls


print("Problem 1")
print("These are my transition matrices just as a sanity check")
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
print("")
SupportMarkov.print_outcomes(simOutputs, 'No treatment:')
SupportMarkov.print_outcomes(simOutputs2, 'Anticoagulation treatment:')

print("Problem 2")
SupportMarkov.print_comparative_outcomes(simOutputs, simOutputs2)

print("")
print("Problem 3")
SupportMarkov.report_CEA_CBA(simOutputs, simOutputs2)
print("See diagram for visual")
print("See table for exact answer")


SupportMarkov.print_table(simOutputs, simOutputs2)

print("")
print("Problem 4")
print("See diagram for for cost-benefit")
print("I would be willing to pay for this at around $20,280 per QALY")
print("")
print("Thanks Reza for your help")
