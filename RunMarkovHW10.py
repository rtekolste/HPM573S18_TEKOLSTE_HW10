import ParameterClassesHW10 as P
import MarkovClassesHW10 as MarkovCls
import SupportMarkovHW10 as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs


print("Problem 1")

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

