"""
Description:   Write a brief description of the script's purpose here.
Author:        David Jiménez Cooper - SpiderCoop
Date:          2026-10-10
"""

from langgraph.graph import END, START, StateGraph

from cv_analyzer.llm_workflows.alignment_analyst import alignment_analysis
from cv_analyzer.llm_workflows.cv_extractor import extraer_cv
from cv_analyzer.llm_workflows.pt_extractor import extraer_pt
from cv_analyzer.states.alignment_state import AlignmentState

# Creamos el grafo de estados para el análisis del candidato
alignment_graph = StateGraph(AlignmentState)

# Definimos los nodos del grafo de análisis del candidato
alignment_graph.add_node("Extraer información del puesto", extraer_pt)
alignment_graph.add_node("Extraer información del CV", extraer_cv)
alignment_graph.add_node("Evaluar ajuste del candidato", alignment_analysis)

# Definimos las transiciones entre los nodos del grafo de análisis del candidato
alignment_graph.add_edge(START, "Extraer información del puesto")
alignment_graph.add_edge("Extraer información del puesto", "Extraer información del CV")
alignment_graph.add_edge("Extraer información del CV", "Evaluar ajuste del candidato")
alignment_graph.add_edge("Evaluar ajuste del candidato", END)
alignment_graph = alignment_graph.compile()
