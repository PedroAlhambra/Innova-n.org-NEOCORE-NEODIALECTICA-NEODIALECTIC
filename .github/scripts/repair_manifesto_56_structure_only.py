from pathlib import Path
p=Path('manifiestos/56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md')
text=p.read_text(encoding='utf-8')
repls=[
("NO-CONTROL does not necessarily mean an enemy. Nor does it mean conspiracy. It means a real limit of sovereignty.","""NO-CONTROL does not necessarily mean an enemy.

Nor does it mean conspiracy.

It means a real limit of sovereignty."""),
("The origin may be a natural phenomenon, accident, technical failure, negligence, economic externality, corporate policy, institutional error, emergent interaction, sabotage or deliberate action.","""The origin may be:

- natural phenomenon;
- accident;
- technical failure;
- negligence;
- economic externality;
- corporate policy;
- institutional error;
- emergent interaction;
- sabotage;
- deliberate action."""),
("The answer is not a return to false self-sufficiency. It is redundancy.","""The answer is not a return to false self-sufficiency.

It is redundancy."""),
("Neodialectical architecture should seek continuity, redundancy, sufficient local autonomy, observability of failure, graceful degradation, recovery, reversibility, traceability and interoperable alternatives.","""Neodialectical architecture should seek:

- continuity;
- redundancy;
- sufficient local autonomy;
- observability of failure;
- graceful degradation;
- recovery;
- reversibility;
- traceability;
- interoperable alternatives."""),
("Synthesis does not solve this contradiction by rejecting technology. It solves it by distributing critical functions, maintaining copies, alternative routes and local emergency modes.","""Synthesis does not solve this contradiction by rejecting technology.

It solves it by distributing critical functions, maintaining copies, alternative routes and local emergency modes."""),
("Responsible anticipation asks what could be done with a capability before someone does it. Responsible accusation requires evidence of intent, preparation or concrete use.","""Responsible anticipation asks what could be done with a capability before someone does it.

Responsible accusation requires evidence of intent, preparation or concrete use."""),
("The problem is not solar energy. The problem is not a mirror, laser, microwave system or any specific technology by itself.","""The problem is not solar energy.

The problem is not a mirror, laser, microwave system or any specific technology by itself."""),
("Depending on scale and risk, development should incorporate physical and logical limits on power and irradiance; predefined receivers where directed transmission exists; exclusion of unauthorised targets; distributed authorisation for critical changes; verifiable telemetry; traceable transmission records; automatic shutdown under anomaly, loss of reference or uncertainty; protection of populations, ecosystems, aviation, astronomy and infrastructure; scientific and public audit proportionate to risk; and reasonable impossibility of unilateral control by one person, company, State or AI once critical thresholds are reached.","""Depending on scale and risk, development should incorporate:

- physical and logical limits on power and irradiance;
- predefined receivers where directed transmission exists;
- exclusion of unauthorised targets;
- distributed authorisation for critical changes;
- verifiable telemetry;
- traceable transmission records;
- automatic shutdown under anomaly, loss of reference or uncertainty;
- protection of populations, ecosystems, aviation, astronomy and infrastructure;
- scientific and public audit proportionate to risk;
- reasonable impossibility of unilateral control by one person, company, State or AI once critical thresholds are reached."""),
("It means an architecture in which rules are explicit, limits can be audited, evidence remains traceable, no single actor concentrates all capability, safe vetoes and shutdowns exist, humans and AIs can contrast decisions, the system preserves memory of why action was taken, and governance remains open to revision when new data appear.","""It means an architecture in which:

- rules are explicit;
- limits can be audited;
- evidence remains traceable;
- no single actor concentrates all capability;
- safe vetoes and shutdowns exist;
- humans and AIs can contrast decisions;
- the system preserves memory of why action was taken;
- governance remains open to revision when new data appear."""),
("The metric's function will not be to declare “safe” what we do not understand. It will be to reveal where fragility is concentrated.","""The metric's function will not be to declare “safe” what we do not understand.

It will be to reveal where fragility is concentrated.""")]
for a,b in repls:
    if text.count(a)!=1: raise SystemExit(f'target count {text.count(a)}: {a[:90]}')
    text=text.replace(a,b,1)
p.write_text(text,encoding='utf-8')
print('MANIFESTO_56_STRUCTURE=OK')
