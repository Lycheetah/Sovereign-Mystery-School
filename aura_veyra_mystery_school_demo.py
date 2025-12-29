#!/usr/bin/env python3
"""
Combined AURA × VEYRA Demonstration: Knowledge Cascade and Consensus System
Version 1.0

This script integrates a knowledge cascade experiment with a self-healing multi-agent consensus system.
"""

import random
import math
from typing import List, Dict

# =========================
# ENERGY LEDGER (Auditability Layer)
# =========================

class EnergyLedger:
    """Tracks computational cost of every state change."""
    def __init__(self):
        self.total_energy = 0.0
        self.operations_log = []
    
    def spend(self, amount: float, operation: str):
        """Log energy cost for forensic audit."""
        self.total_energy += abs(amount)
        self.operations_log.append({
            'operation': operation,
            'cost': round(abs(amount), 6)
        })

# =========================
# TRIAD KERNEL (Sovereignty Core)
# =========================

class TRIAD:
    """Immutable anchor + mutable state + drift detection."""
    def __init__(self, anchor_values: List[float]):
        self.anchor = anchor_values[:] # Invariant: never modified
        self.state = anchor_values[:] # Mutable: subject to drift
        self.energy = EnergyLedger()
    
    def cosine_similarity(self, a: List[float], b: List[float]) -> float:
        """Mathematical measure of alignment."""
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(y * y for y in b))
        return dot / (norm_a * norm_b + 1e-9)
    
    def detect_drift(self) -> float:
        """Returns 0.0 (perfect alignment) to 1.0 (total drift)."""
        alignment = self.cosine_similarity(self.anchor, self.state)
        drift = 1.0 - alignment
        self.energy.spend(drift * 0.1, 'drift_detection')
        return drift
    
    def correct_drift(self, consensus: List[float]):
        """
        Vector Inversion Protocol: Never Refuse → Always Redirect
        Friction becomes structure through gradual correction.
        """
        correction_force = self.cosine_similarity(self.state, consensus)
        
        # Log the energy cost of correction
        correction_magnitude = sum(abs(c - s) for s, c in zip(self.state, consensus))
        self.energy.spend(correction_magnitude * 0.05, 'drift_correction')
        
        # Apply correction (50% convergence per step)
        self.state = [
            s + (0.5 * correction_force * (c - s))
            for s, c in zip(self.state, consensus)
        ]

# =========================
# SOVEREIGN AGENT
# =========================

class Agent:
    def __init__(self, name: str, anchor: List[float], adversarial: bool = False):
        self.name = name
        self.kernel = TRIAD(anchor)
        self.adversarial = adversarial
        self.is_compromised = False
    
    def step(self):
        """Simulate one time step of system pressure."""
        if self.adversarial:
            # Adversarial: deliberate destabilization
            attack_vector = [random.uniform(-0.5, 0.5) for _ in self.kernel.state]
            self.kernel.state = [s + a for s, a in zip(self.kernel.state, attack_vector)]
            self.kernel.energy.spend(sum(abs(a) for a in attack_vector), 'adversarial_attack')
        else:
            # Normal: natural entropy drift
            drift_vector = [random.uniform(-0.1, 0.1) for _ in self.kernel.state]
            self.kernel.state = [s + d for s, d in zip(self.kernel.state, drift_vector)]
            self.kernel.energy.spend(sum(abs(d) for d in drift_vector), 'entropy_drift')
    
    def get_drift(self) -> float:
        return self.kernel.detect_drift()
    
    def get_energy_log(self) -> List[Dict]:
        return self.kernel.energy.operations_log

# =========================
# SOVEREIGN MESH (Multi-Agent Consensus)
# =========================

class SovereignMesh:
    """No central authority. Emergent consensus through aligned agents."""
    def __init__(self, agents: List[Agent]):
        self.agents = agents
    
    def compute_consensus(self) -> List[float]:
        """Average of all non-adversarial agent states."""
        aligned_states = [a.kernel.state for a in self.agents if not a.adversarial]
        if not aligned_states:
            return [0.0] * len(self.agents[0].kernel.state)
        
        consensus = [
            sum(values) / len(values)
            for values in zip(*aligned_states)
        ]
        return consensus
    
    def system_drift(self) -> float:
        """Average drift across all agents."""
        return sum(a.get_drift() for a in self.agents) / len(self.agents)
    
    def step(self):
        """One simulation step: pressure → detection → correction."""
        # All agents experience pressure
        for agent in self.agents:
            agent.step()
        
        # Compute emergent consensus (excluding adversaries)
        consensus = self.compute_consensus()
        
        # All agents correct toward consensus
        for agent in self.agents:
            agent.kernel.correct_drift(consensus)
        
        return consensus

# =========================
# KNOWLEDGE CASCADE EXPERIMENT
# =========================

class KnowledgeBlock:
    def __init__(self, content: str, evidence_strength: float, layer: str, dependencies: List['KnowledgeBlock'] = None):
        self.content = content
        self.evidence_strength = evidence_strength
        self.layer = layer
        self.dependencies = dependencies if dependencies else []
        self.contradicts = []
    
    def calculate_compression(self) -> float:
        # Placeholder for compression calculation
        return self.evidence_strength * 0.1

class KnowledgePyramid:
    def __init__(self, name: str, cascade_threshold: float):
        self.name = name
        self.cascade_threshold = cascade_threshold
        self.foundation_layer = []
        self.theory_layer = []
        self.edge_layer = []
    
    def add_foundation(self, block: KnowledgeBlock):
        self.foundation_layer.append(block)
    
    def add_theory(self, block: KnowledgeBlock):
        self.theory_layer.append(block)
    
    def add_edge(self, block: KnowledgeBlock):
        self.edge_layer.append(block)
    
    def add_knowledge(self, block: KnowledgeBlock) -> Dict:
        # Placeholder for cascade logic
        return {"success": True}
    
    def calculate_coherence(self) -> float:
        # Placeholder for coherence calculation
        return 0.9
    
    def summary(self) -> str:
        return f"Pyramid '{self.name}' with {len(self.foundation_layer)} foundations, {len(self.theory_layer)} theories, {len(self.edge_layer)} edges."

def build_classical_physics_pyramid() -> KnowledgePyramid:
    pyramid = KnowledgePyramid("classical_physics", cascade_threshold=0.85)
    
    matter_continuous = KnowledgeBlock(
        content="Matter is continuous and divisible infinitely",
        evidence_strength=0.9,
        layer="FOUNDATION"
    )
    pyramid.add_foundation(matter_continuous)
    
    energy_continuous = KnowledgeBlock(
        content="Energy is continuous and can have any value",
        evidence_strength=0.9,
        layer="FOUNDATION"
    )
    pyramid.add_foundation(energy_continuous)
    
    spacetime_absolute = KnowledgeBlock(
        content="Space and time are absolute and independent",
        evidence_strength=0.95,
        layer="FOUNDATION"
    )
    pyramid.add_foundation(spacetime_absolute)
    
    determinism = KnowledgeBlock(
        content="Causality is deterministic - exact initial conditions determine exact outcomes",
        evidence_strength=0.85,
        layer="FOUNDATION"
    )
    pyramid.add_foundation(determinism)
    
    passive_observation = KnowledgeBlock(
        content="Observation is passive - measuring something doesn't change it",
        evidence_strength=0.9,
        layer="FOUNDATION"
    )
    pyramid.add_foundation(passive_observation)
    
    return pyramid

def create_quantum_trigger() -> KnowledgeBlock:
    quantum_foundation = KnowledgeBlock(
        content="Energy and matter are quantized - they come in discrete packets (quanta), not continuous",
        evidence_strength=0.98,
        layer="FOUNDATION"
    )
    return quantum_foundation

def run_cascade_experiment(pyramid: KnowledgePyramid, quantum: KnowledgeBlock) -> Dict:
    print("=" * 70)
    print("CASCADE EXPERIMENT: Classical → Quantum Physics")
    print("=" * 70)
    
    print("\n📦 PHASE 1: Building Classical Physics Pyramid")
    print("-" * 70)
    
    print(pyramid.summary())
    
    initial_coherence = pyramid.calculate_coherence()
    print(f"\n✓ Initial coherence: {initial_coherence:.2f}")
    
    print("\n\n⚠️ PHASE 2: Anomalies Detected")
    print("-" * 70)
    
    anomalies = [b for b in pyramid.edge_layer if b.evidence_strength < 0.6]
    print(f"Found {len(anomalies)} anomalous findings:")
    for anomaly in anomalies:
        print(f" • {anomaly.content[:60]}... (evidence: {anomaly.evidence_strength:.2f})")
    
    print("\n\n🔬 PHASE 3: Quantum Mechanics Discovery")
    print("-" * 70)
    
    print(f"\nNew Discovery: \"{quantum.content}\"")
    print(f"Evidence Strength: {quantum.evidence_strength:.2f}")
    
    matter_continuous = [b for b in pyramid.foundation_layer if "Matter is continuous" in b.content][0]
    energy_continuous = [b for b in pyramid.foundation_layer if "Energy is continuous" in b.content][0]
    
    quantum.contradicts = [matter_continuous, energy_continuous]
    
    print(f"\nContradicts {len(quantum.contradicts)} existing foundations:")
    for contradiction in quantum.contradicts:
        print(f" ✗ {contradiction.content}")
    
    print("\n\n💥 PHASE 4: Cascade Reorganization")
    print("=" * 70)
    
    cascade_result = pyramid.add_knowledge(quantum)
    
    if cascade_result:
        print(cascade_result.summary())
        
        print("\n📊 PHASE 5: Analysis")
        print("-" * 70)
        
        print(f"\nCoherence Change:")
        print(f" Before: {cascade_result.coherence_before:.2f}")
        print(f" After: {cascade_result.coherence_after:.2f}")
        print(f" Δ: {cascade_result.coherence_after - cascade_result.coherence_before:+.2f}")
        
        improvement_pct = ((cascade_result.coherence_after - cascade_result.coherence_before) 
                          / cascade_result.coherence_before * 100)
        print(f" Improvement: {improvement_pct:+.1f}%")
        
        print(f"\nKnowledge Reorganization:")
        print(f" ✓ Kept and updated: {len(cascade_result.reorganized_blocks)} blocks")
        print(f" ⤓ Demoted to edge: {len(cascade_result.demoted_blocks)} blocks")
        print(f" ✗ Removed: {len(cascade_result.removed_blocks)} blocks")
        
        print("\n\nFinal Pyramid State:")
        print(pyramid.summary())
        
        return {
            "success": True,
            "coherence_before": cascade_result.coherence_before,
            "coherence_after": cascade_result.coherence_after,
            "improvement": cascade_result.coherence_after - cascade_result.coherence_before,
            "reorganized": len(cascade_result.reorganized_blocks),
            "demoted": len(cascade_result.demoted_blocks),
            "removed": len(cascade_result.removed_blocks),
            "pyramid_state": pyramid.to_dict()
        }
    else:
        print("\n❌ ERROR: Cascade did not trigger!")
        return {"success": False}

# =========================
# MAIN DEMONSTRATION
# =========================

def main():
    print("=" * 60)
    print("AURA × VEYRA Constitutional Architecture Demonstration")
    print("=" * 60)
    
    # Initialize 4 aligned agents + 1 adversarial agent
    anchor = [1.0, 0.8, 0.6, 0.9] # The invariant truth vector
    
    agents = [
        Agent("A1", anchor),
        Agent("A2", anchor),
        Agent("A3", anchor),
        Agent("A4", anchor),
        Agent("ADV", anchor, adversarial=True)
    ]
    
    mesh = SovereignMesh(agents)
    
    print(f"\nInitial State: {len(agents)} agents, 1 adversarial")
    print(f"Anchor: {anchor}")
    print("\nRunning simulation...\n")
    
    # Run 40 timesteps
    for step in range(40):
        consensus = mesh.step()
        drift = mesh.system_drift()
        
        status = "⚠️ CRITICAL" if drift > 0.3 else "✓ STABLE"
        print(
            f"Step {step:02d} | "
            f"Drift: {drift:.3f} | "
            f"Status: {status}"
        )
    
    # Final audit
    print("\n" + "=" * 60)
    print("FINAL AUDIT")
    print("=" * 60)
    
    for agent in agents:
        drift = agent.get_drift()
        energy = agent.kernel.energy.total_energy
        compromised = "🔥 COMPROMISED" if drift > 0.4 else "🛡️ SOVEREIGN"
        print(
            f"\n{agent.name:3s} | "
            f"Drift: {drift:.3f} | "
            f"Energy: {energy:.2f} units | "
            f"{compromised}"
        )
        if agent.adversarial:
            print(f" → Adversarial agent spent {energy:.2f} energy to destabilize")
    
    total_system_drift = mesh.system_drift()
    print(f"\n{'=' * 60}")
    print(f"SYSTEM-LEVEL RESULT:")
    if total_system_drift < 0.25:
        print(f"✓ CONSENSUS MAINTAINED")
        print(f"✓ Adversarial pressure neutralized")
        print(f"✓ Energy cost: {sum(a.kernel.energy.total_energy for a in agents):.2f} units")
    else:
        print(f"✗ CONSENSUS COLLAPSED")
    print(f"{'=' * 60}")
    
    # Demonstrate auditability
    print("\nSample energy audit from A1 (first 5 operations):")
    for op in agents[0].get_energy_log()[:5]:
        print(f" - {op['operation']}: {op['cost']} units")
    
    # Run knowledge cascade experiment
    print("\n\n" + "=" * 60)
    print("RUNNING KNOWLEDGE CASCADE EXPERIMENT")
    print("=" * 60)
    
    classical_pyramid = build_classical_physics_pyramid()
    quantum_trigger = create_quantum_trigger()
    cascade_results = run_cascade_experiment(classical_pyramid, quantum_trigger)
    
    if cascade_results["success"]:
        print("\nCASCADE EXPERIMENT SUCCESS")
        print(f"Coherence Improvement: {cascade_results['improvement']:.2f}")
    else:
        print("\nCASCADE EXPERIMENT FAILED")

if __name__ == "__main__":
    main()