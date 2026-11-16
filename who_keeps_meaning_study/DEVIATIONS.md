# Deviations and clarifications after freezing (commit e4c410c)

All written before reading any confirmatory output.

1. **Panel sample age.** Baseline (wave 1) restricted to ages 25–62 so respondents stay ≤64 by wave 3 (two-year
   spacing). Pre-registration said 25–64 without addressing ageing across waves.
2. **Panel weights.** Panel FE models are unweighted. The pre-registration specified `wtssps` for the cross-section
   but said nothing about panel weights; GSS panel weights (`wtpan*`) are for population totals, not FE.
3. **H5b operationalisation.** "Income moderation" = AME penalty at top tercile minus at bottom tercile, divided by
   the outcome's weighted SD, compared in absolute value between O2b and O1. The two models are fitted separately,
   so the comparison's uncertainty is approximated by independent parameter simulations (a conservative choice
   would be a joint bootstrap; noted as a limitation).
4. **H7 sample.** "Exit" estimated as the within-person `NW` coefficient among people working at wave 1 (so the
   coefficient reflects exits, plus any later re-entry).
5. **P1 implementation.** People working at waves 1 and 2 with all three waves observed; O1(w2) − O1(w1) regressed
   on NW at wave 3. A non-zero coefficient = decline before exit.
6. **Code fix (no change to the plan):** first run crashed in the exploratory by-sex split because the female dummy
   is constant within one sex; constant columns are now dropped from the design matrix.
