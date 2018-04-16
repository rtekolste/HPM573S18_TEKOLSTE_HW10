import InputDataHW10 as Settings
import scr.FormatFunctions as F
import scr.StatisticalClasses as Stat
import scr.EconEvalClasses as Econ
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs


def print_outcomes(simOutput, therapy_name):
    """ prints the outcomes of a simulated cohort
    :param simOutput: output of a simulated cohort
    :param therapy_name: the name of the selected therapy
    """
    # mean and confidence interval text of patient survival time
    survival_mean_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_survival_times().get_mean(),
        interval=simOutput.get_sumStat_survival_times().get_t_CI(alpha=Settings.ALPHA),
        deci=2)

    # mean and confidence interval text of time to stroke
    strokes_mean_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_count_strokes().get_mean(),
        interval=simOutput.get_sumStat_count_strokes().get_t_CI(alpha=Settings.ALPHA),
        deci=2)

        # mean and confidence interval text of discounted total utility
    utility_mean_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_discounted_utility().get_mean(),
        interval=simOutput.get_sumStat_discounted_utility().get_t_CI(alpha=Settings.ALPHA),
        deci=2)

    # print outcomes
    print(therapy_name)
    print("  Estimate of mean and {:.{prec}%} confidence interval of survival time:".format(1 - Settings.ALPHA, prec=0),
          survival_mean_CI_text)
    print("  Estimate of mean and {:.{prec}%} confidence interval of time to stroke:".format(1 - Settings.ALPHA, prec=0),
          strokes_mean_CI_text)
    print("  Estimate of discounted utility and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          utility_mean_CI_text)
    print("")


def print_comparative_outcomes(simOutputs_none, simOutputs_anticoag):
    """ prints average increase in survival time, discounted cost, and discounted utility
    under combination therapy compared to none therapy
    :param simOutputs_none: output of a cohort simulated under no therapy
    :param simOutputs_anticoag: output of a cohort simulated under combination therapy
    """

    # increase in survival time under combination therapy with respect to no therapy
    if Settings.PSA_ON:
        increase_survival_time = Stat.DifferenceStatPaired(
            name='Increase in survival time',
            x=simOutputs_anticoag.get_survival_times(),
            y_ref=simOutputs_none.get_survival_times())
    else:
        increase_survival_time = Stat.DifferenceStatIndp(
            name='Increase in survival time',
            x=simOutputs_anticoag.get_survival_times(),
            y_ref=simOutputs_none.get_survival_times())

    # estimate and CI
    estimate_CI = F.format_estimate_interval(
        estimate=increase_survival_time.get_mean(),
        interval=increase_survival_time.get_t_CI(alpha=Settings.ALPHA),
        deci=2)
    print("Average increase in survival time "
          "and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          estimate_CI)

    # increase in discounted total cost under combination therapy with respect to no therapy
    if Settings.PSA_ON:
        increase_discounted_cost = Stat.DifferenceStatPaired(
            name='Increase in discounted cost',
            x=simOutputs_anticoag.get_costs(),
            y_ref=simOutputs_none.get_costs())
    else:
        increase_discounted_cost = Stat.DifferenceStatIndp(
            name='Increase in discounted cost',
            x=simOutputs_anticoag.get_costs(),
            y_ref=simOutputs_none.get_costs())

    # estimate and CI
    estimate_CI = F.format_estimate_interval(
        estimate=increase_discounted_cost.get_mean(),
        interval=increase_discounted_cost.get_t_CI(alpha=Settings.ALPHA),
        deci=0,
        form=F.FormatNumber.CURRENCY)
    print("Average increase in discounted cost "
          "and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          estimate_CI)

    # increase in discounted total utility under combination therapy with respect to no therapy
    if Settings.PSA_ON:
        increase_discounted_utility = Stat.DifferenceStatPaired(
            name='Increase in discounted utility',
            x=simOutputs_anticoag.get_utilities(),
            y_ref=simOutputs_none.get_utilities())
    else:
        increase_discounted_utility = Stat.DifferenceStatIndp(
            name='Increase in discounted cost',
            x=simOutputs_anticoag.get_utilities(),
            y_ref=simOutputs_none.get_utilities())

    # estimate and CI
    estimate_CI = F.format_estimate_interval(
        estimate=increase_discounted_utility.get_mean(),
        interval=increase_discounted_utility.get_t_CI(alpha=Settings.ALPHA),
        deci=2)
    print("Average increase in discounted utility "
          "and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          estimate_CI)
