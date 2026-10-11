# Appendix F — Key formulas and rules of thumb

## Summaries
| Quantity | Formula | Grade |
|---|---|---|
| mean | x̄ = Σx ÷ n | 8 |
| median | middle of sorted values; position (n + 1) ÷ 2 | 8 |
| range | max − min | 8 |
| quartiles, IQR | Q1, Q3 (medians of lower/upper halves); IQR = Q3 − Q1 | 9–10 |
| outlier fences | Q1 − 1.5 × IQR, Q3 + 1.5 × IQR | 9–10 |
| variance, SD (sample) | s² = Σ(x − x̄)² ÷ (n − 1); s = √s² | 10 |
| z-score | z = (x − x̄) ÷ s | 10 |
| coefficient of variation | s ÷ x̄ | 10 |
| 68–95 rule | bell-shaped data: ≈ 68% within 1 SD, ≈ 95% within 2 SD | 10 |

## Rates and change
| Quantity | Formula | Grade |
|---|---|---|
| rate | numerator ÷ denominator × 100 / 1,000 / 100,000 | 8–9 |
| ratio | e.g. sex ratio = males ÷ females × 100 | 9 |
| weighted group rate | Σ numerators ÷ Σ denominators | 9 |
| percentage points | new % − old % | 8 |
| percent change | (new − old) ÷ old × 100 | 8 |
| annual growth rate | (new ÷ old)^(1/years) − 1 | 9 |
| index number | value ÷ base value × 100 | 9 |
| angle in a pie chart | share × 360° | 8 |

## Relationships and models
| Quantity | Formula | Grade |
|---|---|---|
| correlation | r = Σ(z_x × z_y) ÷ (n − 1), −1 ≤ r ≤ 1 | 9–10 |
| least-squares line | ŷ = a + b x; b = r × s_y ÷ s_x; a = ȳ − b x̄ | 10 |
| residual | y − ŷ | 10 |
| R² | 1 − Σ(residual²) ÷ Σ(y − ȳ)²; for one predictor R² = r² | 10–11 |
| logistic function | p = 1 ÷ (1 + e^(−z)), z = b₀ + b₁x₁ + … | 12 |
| odds, odds ratio | odds = p ÷ (1 − p); OR per unit = e^b | 12 |
| MAE, RMSE | mean |y − ŷ|; √mean (y − ŷ)² | 12 |

## Uncertainty and testing
| Quantity | Formula / rule | Grade |
|---|---|---|
| standard error of a mean | ≈ s ÷ √n (quadruple n → halve SE) | 11 |
| rough 95% interval | estimate ± 2 × SE | 11 |
| bootstrap 95% CI | 2.5th to 97.5th percentiles of bootstrap statistics | 11 |
| permutation p-value | share of shuffled statistics at least as extreme as observed (two-sided: compare absolute values) | 11 |
| SE of a proportion | ≈ √(p(1 − p) ÷ n) | 12 |

## Classification metrics
| Metric | Formula |
|---|---|
| accuracy | (TP + TN) ÷ all |
| precision | TP ÷ (TP + FP) |
| recall (sensitivity) | TP ÷ (TP + FN) |
| specificity | TN ÷ (TN + FP) |
| F1 | 2 × precision × recall ÷ (precision + recall) |
| selection rate | flagged ÷ group size |

## Time and place
| Quantity | Formula | Grade |
|---|---|---|
| BS → AD year | − 57 (mid-April to December), − 56 (January to mid-April) | 9 |
| additive seasonal index | month mean − overall mean (sum = 0) | 11 |
| multiplicative seasonal index | month mean ÷ overall mean (average = 1) | 11 |
| anomaly | observed − baseline for that month | 10 |
| trend per decade | slope (per year) × 10 | 10 |
| km per degree | latitude ≈ 111 km; longitude ≈ 111 × cos(latitude) km | 11 |
| haversine distance | d = 2R·arcsin √(sin²(Δφ/2) + cos φ₁ cos φ₂ sin²(Δλ/2)), R = 6,371 km | 11 |

## Unit conversions often met in Nepali data
1 lakh = 100,000 · 1 crore = 10,000,000 · 1 ropani = 508.72 m² · 1 bigha = 6,772.63 m² · rain mm/day × days = mm per
month · 1 µg/m³ = one-millionth of a gram per cubic metre.
