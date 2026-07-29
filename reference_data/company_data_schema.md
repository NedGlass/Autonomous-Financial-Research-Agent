## Reference data notes

Notes on how company_data.json was built, and things worth remembering later.

## Source documents

Not every company files the same type of document. Shell, BP, National Grid, SSE and Drax are UK-listed so they publish an Annual Report and Accounts rather than a US-style 10-K. BP's is actually combined with Form 20-F since BP also trades as an ADR on the NYSE, so it has to satisfy SEC disclosure rules too. ExxonMobil and NextEra are US-listed so their filing is a proper 10-K, which is organised into numbered Items. Reserves and production both live under Item 2, Properties. TotalEnergies, RWE and Ørsted each publish their own home-market annual report.

## Ownership basis for reserves and production

For all four oil and gas companies I used the combined total (subsidiaries plus their share of joint ventures/equity-accounted entities), not subsidiaries alone. Shell calls this "Totals," BP calls it "Total subsidiaries and equity-accounted entities," Exxon calls it "Total Proved Reserves." Different labels, same idea. Went with the combined figure everywhere so the companies are actually comparable to each other.

## BOE conversion isn't the same across companies

For example, BP states they convert gas to boe at 5,800 cubic feet per barrel. ExxonMobil uses 6,000. Found both numbers directly in their own reports, not assumed. So even though the reserves and production figures all end up labelled "boe," they're not built on quite the same assumption underneath. Worth mentioning as a caveat in the final report rather than pretending the numbers are perfectly apples to apples.

## Production figures needed different handling per company

Shell's table only gives an annual total for the year, so I divided by 365 to get a daily rate (2025 isn't a leap year, so 365 is exact). BP already reports a headline "oil and gas production (mboe/d)" figure as a native daily rate, so no dividing needed there, just converting the scale from thousands. Exxon's the same, already daily, just needed the thousands conversion. So the three companies needed three slightly different paths to end up in the same final unit.

## Units

Everything is stored as actual raw figures, real barrels. Real barrels per day, not in the millions or thousands scale the source tables use. Converted this at entry time. Reasoning is that the field names (proven_reserves_boe, production_boed) already imply real units, and there's no way to leave a note in JSON saying "this is actually in millions" so better to just store it properly and avoid the ambiguity entirely.

## Rounding

Production figures are rounded to whole numbers, not kept to several decimal places. The source tables themselves are only accurate to the nearest million or thousand boe, so carrying decimals further than that doesn't add real precision, just makes it look more precise than it is.

## What doesn't belong in this file

Reserve life (reserves divided by production) isn't stored here, it's a calculated figure, not something actually printed in an annual report. So it gets calculated later instead. Converting a single sourced figure into a different unit (eg. annual to daily) is fine to do here, but combining two separate figures into a new metric isn't. This keeps the file as raw data rather than a mix of raw and derived.

## Generation capacity and mix (utilities and renewables)

For the six non oil and gas companies, capacity_mw is the company's own reported generation capacity in MW, not output. Capacity is what a plant could produce running flat out. GWh or TWh figures elsewhere in these reports are actual output and shouldn't be confused with this. mix_pct splits that capacity by technology: gas, wind, nuclear and hydro get their own field, everything else (solar, biomass, battery storage, and lignite/coal where the amount was too small to bother with its own field) goes into other. A company with a big other number isn't necessarily uncertain data, it just means their fleet leans on something outside the five named buckets.

## Where the utility and renewable figures came from

All sourced from publicly available annual reports from each company website. Except NextEra Energy, which wasn't pulled from an annual report and came from the SEC 10-K on EDGAR.

## Calls made on ambiguous headline capacity figures

A few companies didn't have one obvious capacity number, so here's the reasoning behind what got picked in case it needs defending later.

SSE's report had four different capacity like numbers floating around: 10.8GW, 5.3GW, and two forward targets (7GW and 8GW). The 10.8GW turned out to be renewable capacity connected to SSEN Transmission's grid, which includes third party generation, not SSE's own fleet, so a network metric, not a generation one. The 7GW and 8GW are FY28 and FY29 targets, not current figures. What actually went in is SSE Renewables' own "total renewable generation capacity (inc. storage)" of 5,279MW plus SSE Thermal's "total thermal generation capacity" of 6,253MW, for 11,532MW combined.

Drax's report quotes 0.9GW of OCGTs and 0.7GW of BESS alongside the actual operating assets, but both are explicitly labelled "when fully commissioned," meaning under construction. Only counted what's actually built and running: 2.6GW biomass at Drax Power Station, 0.4GW Cruachan pumped storage, 0.1GW Lanark and Galloway hydro, so 3.1GW total.

Iberdrola's five geographic segment tables (Spain, UK, US, Brazil, and its international arm) add up to 55,744MW, which is about 2,600MW short of the 58,343MW group total quoted elsewhere in the report. Likely Neoenergia (mentioned in a footnote as an inorganic investment) and other minority stakes that aren't broken out by technology in this particular report. Mix percentages are based on the 55,744MW segment total since that's the only figure with a technology breakdown, so treat them as approximate rather than exact shares of the full 58,343MW.

RWE's "other" bucket is unusually big at 37%, worth knowing why. It's not just solar and biomass like most companies, it also swallows 5,832MW of lignite (coal), which RWE still runs a meaningful amount of. Might be worth pulling lignite into its own line in a future version of the schema rather than leaving it buried in other.

## A note on fiscal_year

Kept fiscal_year as a plain number everywhere, matching whatever year each company puts on its own cover page (so SSE is 2026, since that's what its "Annual Report 2026" calls itself, even though the underlying period is April 2025 to March 2026). The actual reporting period for non-calendar year companies is noted here rather than in the JSON, since mixing a number and a "2025/26, year ended March" style string across entries would make fiscal_year inconsistent to work with in code later.

## Low-carbon capex and emissions intensity

Two new blocks per company: capex and emissions. Same idea as everything else in this file, JSON can't hold the reasoning so it lives here.

## These didn't always come from the same document as reserves and production

For the four oil and gas companies especially, the annual report used for reserves and production isn't necessarily where the capex split or emissions figure came from. BP's capex split and its per-boe emissions figure came from the Q4/full year 2025 results release and the ESG Datasheet, not the Annual Report and Form 20-F. TotalEnergies' numbers here came from its results release and the Sustainability & Climate progress report, not the Universal Registration Document used for reserves and production. NextEra's total capex figure came out of the cash flow statement in its earnings release rather than the 10-K, since it just wasn't worth pulling the whole filing apart again for one line.

## Low-carbon capex percentage isn't measured the same way twice

Iberdrola, SSE, Ørsted and RWE all report a percentage of capex classified as EU Taxonomy aligned. Same regulatory definition across all four, audited, so these four can actually be compared against each other.

Shell, BP and TotalEnergies each publish a low-carbon capex figure too, but they don't define the boundary the same way. Shell's Low Carbon Energy Solutions line sits inside a broader Renewables and Energy Solutions segment. BP's line is narrower, sitting specifically inside its gas and low carbon energy segment. TotalEnergies' figure is mostly its Integrated Power segment. All three numbers are real, taken straight from what each company reports, but don't stack them against each other like they're measuring the same thing, because they're not.

Exxon, NextEra and Drax don't have anything here at all. Exxon folds low carbon spending into Corporate and Financing rather than breaking it out as its own segment. Checked the 10-K segment note myself, nothing separate there. NextEra doesn't publish a percentage either, even though NEER's spending is overwhelmingly renewables and storage by description alone. Drax doesn't have an equivalent to the EU Taxonomy disclosure since the UK never adopted one, though its annual report does list capex by category (FlexGen, pellet production, BECCS, OCGT) if that's worth coming back to later.

## Emissions intensity, same story

BP and TotalEnergies both publish an actual upstream Scope 1 and 2 emissions figure per boe, 16.5 and 17 kg CO2e/boe, so these two are directly comparable. Shell doesn't use this convention anywhere, I checked the full annual report for any per boe phrasing and there's nothing there. Exxon does publish an intensity figure but on a different basis, tonnes CO2e per 100 tonnes of production rather than per boe, and converting that over would mean guessing at a barrel to tonne density Exxon doesn't actually state, so left it null rather than make that up.

For the power companies, Iberdrola, NextEra, SSE, Ørsted and RWE all publish a straightforward gCO2/kWh figure for their own generation, so these five line up fine against each other. NextEra's is a year behind the rest though, its most recent confirmed figure covers 2024, not 2025. Drax's number isn't a generation figure at all, it's the average emissions intensity of its biomass supply chain (forestry, processing, transport), which is what it's actually required to report under UK biomass rules. Real number, just not the same kind of number as the other five, so don't put it in the same column without saying so.

## Why some of these fields are null

Didn't want to divide two unrelated numbers together to invent a figure a company never actually stated, and didn't want to use a forward spending plan as if it were the year's actual result. So anywhere a number wasn't stated outright, it's null rather than filled in with something close enough. Applies to Exxon's capex split, Exxon's emissions figure in boe terms, NextEra's capex split, and Drax's capex split.

## The basis field

Added a basis tag to both capex and emissions so it's obvious later which numbers can actually sit next to each other in a comparison and which can't, rather than that living in a paragraph somewhere and getting forgotten by the time it ends up in a chart. Capex uses eu_taxonomy_aligned, company_disclosed_segment or not_disclosed. Emissions uses disclosed_upstream_per_boe, disclosed_grid_point_of_generation, disclosed_lifecycle_supply_chain or not_disclosed. Only ever compare numbers that share the same tag.

## Gaps to watch for

NG.L was in the original ticker list but was swapped out for IBE after research confirmed National Grid is primarily a network operator with no disclosed generation mix, unlike the other utilities.

Exxon has no low-carbon capex split and no emissions figure in boe terms. I checked both directly rather than assuming they weren't findable, genuinely not there. NextEra has no low-carbon capex split, and its emissions figure is a year old. Drax has no low-carbon capex split, and its emissions figure is on a different basis to the other power companies.
