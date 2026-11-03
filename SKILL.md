---
name: genpark-personal-agent-ocular-electrooculography-arden-ratio-eog-skill
description: Evaluates Retinal Pigment Epithelium (RPE) standing potential dynamics through Electrooculography (EOG) Light Peak, Dark Trough, and Arden ratio (LP/DT) calculations.
---

# Ocular Electrooculography (EOG) & Arden Ratio Skill

This skill computes electrophysiological standing potential metrics from ocular electrooculography to quantify retinal pigment epithelium (RPE) function and transepithelial potential changes according to ISCEV clinical standards.

## Core Capabilities
- Evaluates Dark Trough ($DT$) and Light Peak ($LP$) standing potential amplitudes in microvolts.
- Computes Arden Ratio ($LP / DT$, normal $\ge 1.80$) and Arden percentage index ($\ge 180\%$).
- Evaluates interocular Arden delta ($\le 0.25$) for asymmetric retinal disease.
- Diagnoses Best vitelliform macular dystrophy (extinguished EOG light peak with preserved full-field ERG).

## Zero-Mock Architecture
Standard Python standard library only with zero external dependencies.
