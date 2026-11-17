import os
from PIL import Image, ImageDraw, ImageFont

output_dir = r"C:\Users\hp\Downloads\IGNIS_Final\docs\architecture"
os.makedirs(output_dir, exist_ok=True)
brain_dir = r"C:\Users\hp\.gemini\antigravity\brain\1fc8e1fb-3344-4a83-8cb7-30f56fe85564"

font_title = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 30)
font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 18)
font_card_title = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 20)
font_body = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 15)
font_code = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 14)

def draw_card(draw, x, y, w, h, title, subtitle, items, border_color="#3b82f6", bg_color="#1e293b"):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=bg_color, outline=border_color, width=2)
    draw.text((x + 16, y + 14), title, fill="#ffffff", font=font_card_title)
    if subtitle:
        draw.text((x + 16, y + 42), subtitle, fill="#94a3b8", font=font_body)
    curr_y = y + 70
    for item in items:
        draw.text((x + 20, curr_y), f"• {item}", fill="#cbd5e1", font=font_code)
        curr_y += 24

# ==================== 1. BACKEND ARCHITECTURE ====================
img1 = Image.new("RGB", (1400, 950), color="#090d16")
d1 = ImageDraw.Draw(img1)
d1.rectangle([0, 0, 1400, 75], fill="#0f172a")
d1.text((30, 20), "IGNIS BACKEND ARCHITECTURE · RaoSpace Labs", fill="#ff6b2c", font=font_title)
d1.text((1050, 26), "NASA Space Apps 2026", fill="#64748b", font=font_sub)

# Top Layer: API & Entrypoints
draw_card(d1, 40, 100, 1320, 130, "1. Client Interface & API Gateways", "FastAPI REST Server (server.py) & Streamlit Bridge (frontend/ignis_client.py)", [
    "GET  /health                   -> Health & config diagnostics (Render alive ping)",
    "POST /api/ask                 -> Asynchronous Multi-Agent execution pipeline",
    "POST /api/search              -> Page-anchored literature retrieval (102 docs / 16,168 chunks)",
    "GET  /api/corpus/stats        -> Corpus health, chunk counts, and retrieval mode"
], border_color="#ff6b2c")

# Middle Layer: Google ADK Engine & Orchestration
draw_card(d1, 40, 250, 645, 230, "2. Google ADK Orchestration Core", "agent.py & orchestration/workflows.py", [
    "google.adk.apps.App: Top-level runtime wrapper with context cache",
    "ContextCacheConfig: Token optimization (cache_intervals=8, ttl=1800s)",
    "Runner & InMemorySessionService: State management & execution logging",
    "Workflow Registry: 7 deterministic routing topologies (A through G)",
    "Dynamic Task Classifier: Routes questions via semantic keyword heuristics"
], border_color="#3b82f6")

draw_card(d1, 715, 250, 645, 230, "3. Context & Token Management", "context/ context_builder.py, summarizer.py, token_manager.py", [
    "ContextBuilder: Builds structured, grounded context per specialist",
    "ConversationSummarizer: Compresses historical interactions & findings",
    "TokenManager: Budget limits (MAX_INPUT: 3500, MAX_OUTPUT: 2048)",
    "ModelConfig: Gemini 3.5 Flash Lite (primary) + Groq (inference fallback)",
    "Cost & Latency Guard: Eliminates redundant agent delegation hops"
], border_color="#8b5cf6")

# Third Layer: 8 Specialist Agents
draw_card(d1, 40, 500, 1320, 240, "4. The 8 Specialist Agents Layer (google.adk.agents.LlmAgent)", "agents/ directory", [
    "Root Agent (ignis)             -> High-level task routing & specialist transfer orchestrator",
    "NASA Research Agent            -> Real-time NASA NTRS search, metadata retrieval & official media",
    "Document Intelligence Agent    -> Experimental conditions & scientific findings extraction from PDF/DOCX",
    "Data Analyst Agent            -> Deterministic statistical math, missing values & correlation matrices",
    "ML Specialist Agent            -> Microgravity ML feasibility assessment & model performance metrics",
    "Knowledge Graph Agent          -> Concept map extraction & Graphviz visualization generation",
    "Multimodal Vision Agent        -> Chart, plot & scientific figure interpretation via Gemini Vision",
    "Fire Safety Agent              -> Exploration mission relevance (ISS, Artemis) & safety evidence gaps",
    "Scientific Reviewer Agent      -> Independent audit gate: claim verification & citation validation"
], border_color="#10b981")

# Bottom Layer: Tools & Data Corpus
draw_card(d1, 40, 760, 1320, 150, "5. Deterministic Tools & NASA NTRS Evidence Corpus", "tools/ & corpus/ store.py", [
    "Deterministic Python Tools: Pure NumPy / SciPy / Sklearn execution (no LLM hallucination for math)",
    "Local NASA Literature Corpus: 102 NASA technical reports, 16,168 page-anchored text passages",
    "Hybrid Vectorizer: TF-IDF index with optional all-MiniLM-L6-v2 dense embeddings",
    "Live API Integrations: NASA Technical Reports Server (NTRS API), NASA Images API, CORE API"
], border_color="#eab308")

p1 = os.path.join(output_dir, "1_backend_architecture.png")
img1.save(p1)
img1.save(os.path.join(brain_dir, "1_backend_architecture.png"))
print("Image 1 saved successfully")

# ==================== 2. GOOGLE ADK WORKFLOW & TOPOLOGY ====================
img2 = Image.new("RGB", (1400, 950), color="#090d16")
d2 = ImageDraw.Draw(img2)
d2.rectangle([0, 0, 1400, 75], fill="#0f172a")
d2.text((30, 20), "GOOGLE ADK MULTI-AGENT TOPOLOGY · IGNIS", fill="#ff6b2c", font=font_title)
d2.text((1050, 26), "Google ADK 2.0 Integration", fill="#64748b", font=font_sub)

# Root Agent Box (Center Top)
d2.rounded_rectangle([420, 95, 980, 215], radius=12, fill="#1e293b", outline="#ff6b2c", width=3)
d2.text((450, 110), "Root Agent: ignis (LlmAgent)", fill="#ff6b2c", font=font_card_title)
d2.text((450, 140), "App(name='ignis', root_agent=root_agent, context_cache_config=...)", fill="#94a3b8", font=font_code)
d2.text((450, 170), "Routes queries & delegates via ADK transfer_to_agent", fill="#cbd5e1", font=font_body)

# Sub-agents Grid (2 rows of 4)
subagents = [
    ("nasa_research_agent", "NTRS Live API & Literature", ["search_scientific_literature", "search_nasa_research", "retrieve_investigation_metadata"], "#3b82f6"),
    ("document_intelligence_agent", "Document & PDF Intelligence", ["load_document", "extract_experimental_conditions", "extract_research_findings"], "#3b82f6"),
    ("data_analyst_agent", "Deterministic Statistics", ["calculate_descriptive_statistics", "analyze_missing_values", "correlation_analysis"], "#10b981"),
    ("ml_agent", "ML Suitability & Evaluation", ["assess_ml_suitability", "evaluate_model_metrics", "recommend_model_family"], "#10b981"),
    ("knowledge_graph_agent", "Concept Map Generator", ["extract_concept_graph", "build_graphviz_dot", "highlight_entities"], "#8b5cf6"),
    ("multimodal_agent", "Gemini Vision Chart Reader", ["analyze_scientific_figure", "extract_axes_and_trends", "identify_data_limits"], "#ec4899"),
    ("fire_safety_agent", "Mission Relevance & Gaps", ["assess_mission_relevance", "identify_safety_evidence_gaps", "spacecraft_hazard_audit"], "#f59e0b"),
    ("scientific_reviewer_agent", "Quality Control & Audit Gate", ["review_scientific_claims", "validate_citations", "identify_unsupported_findings"], "#ef4444"),
]

for idx in range(8):
    col = idx % 4
    row = idx // 4
    x = 40 + col * 335
    y = 260 + row * 260
    d2.line([(700, 215), (x + 155, y)], fill="#334155", width=2)

for idx, (name, role, tools, col_border) in enumerate(subagents):
    col = idx % 4
    row = idx // 4
    x = 40 + col * 335
    y = 260 + row * 260
    draw_card(d2, x, y, 315, 235, name[:24], role, [f"Tools: {len(tools)} registered"] + tools[:2], border_color=col_border)

# Bottom Note
d2.rounded_rectangle([40, 800, 1360, 905], radius=10, fill="#1e293b", outline="#10b981", width=2)
d2.text((60, 815), "Key Google ADK Mechanism: FunctionTool Binding", fill="#10b981", font=font_card_title)
d2.text((60, 848), "Each specialist is initialized with tools=[FunctionTool(fn1), FunctionTool(fn2), ...].", fill="#cbd5e1", font=font_code)
d2.text((60, 873), "The LLM generates structured tool-calls, ADK executes deterministic functions, and injects results back into context.", fill="#94a3b8", font=font_body)

p2 = os.path.join(output_dir, "2_google_adk_workflow.png")
img2.save(p2)
img2.save(os.path.join(brain_dir, "2_google_adk_workflow.png"))
print("Image 2 saved successfully")

# ==================== 3. AGENT COMMUNICATION ====================
img3 = Image.new("RGB", (1400, 950), color="#090d16")
d3 = ImageDraw.Draw(img3)
d3.rectangle([0, 0, 1400, 75], fill="#0f172a")
d3.text((30, 20), "AGENT COMMUNICATION & INFORMATION EXCHANGE · IGNIS", fill="#ff6b2c", font=font_title)
d3.text((1050, 26), "Shared Session Architecture", fill="#64748b", font=font_sub)

# Step 1: Query Input
draw_card(d3, 40, 110, 380, 240, "1. User Query & Session", "orchestration/workflows.py", [
    "User submits scientific question",
    "sid = ignis-wf-<timestamp>",
    "session_service = InMemorySessionService()",
    "session created with app_name='ignis'",
    "ConversationSummarizer tracks question"
], border_color="#ff6b2c")

# Arrow 1 -> 2
d3.polygon([(445, 220), (470, 230), (445, 240)], fill="#ff6b2c")
d3.line([(420, 230), (465, 230)], fill="#ff6b2c", width=4)

# Step 2: Layered Execution
draw_card(d3, 490, 110, 420, 240, "2. Specialist Step (Runner)", "google.adk.runners.Runner", [
    "Runner(agent=specialist, session_service)",
    "ContextBuilder formats input context",
    "Agent runs prompt + calls FunctionTools",
    "Events emitted: ToolCall -> ToolReturn",
    "Findings extracted & validated"
], border_color="#3b82f6")

# Arrow 2 -> 3
d3.polygon([(935, 220), (960, 230), (935, 240)], fill="#3b82f6")
d3.line([(910, 230), (955, 230)], fill="#3b82f6", width=4)

# Step 3: Shared Memory State
draw_card(d3, 980, 110, 380, 240, "3. Shared In-Memory State", "sessions/session_manager.py", [
    "Session state updated synchronously",
    "No file I/O overhead (zero latency)",
    "Step output appended to context log",
    "Conversation history preserved",
    "Step latency & tokens recorded"
], border_color="#10b981")

# Middle Banner: ContextBuilder Pipeline
d3.rounded_rectangle([40, 385, 1360, 585], radius=12, fill="#1e293b", outline="#8b5cf6", width=2)
d3.text((60, 405), "Context Pipeline: How Specialist A Feeds Specialist B", fill="#8b5cf6", font=font_card_title)
d3.text((60, 445), "1. Specialist A (NASA Research): Retrieves 5 NTRS papers and returns verified excerpts with page anchors [p.4, p.11].", fill="#cbd5e1", font=font_body)
d3.text((60, 480), "2. ContextBuilder: Sanitizes raw payload, extracts findings, formats structured context for Specialist B.", fill="#cbd5e1", font=font_body)
d3.text((60, 515), "3. Specialist B (Fire Safety): Interprets the findings specifically in the context of spacecraft exploration risks.", fill="#cbd5e1", font=font_body)
d3.text((60, 550), "4. Specialist C (Reviewer): Audits claims against cited passages; if ungrounded, outputs verdict: REJECT / REVISE.", fill="#cbd5e1", font=font_body)

# Bottom: Example Data Flow (Workflow C: Comparative Experiment)
draw_card(d3, 40, 615, 1360, 280, "Concrete Example: Workflow C (Comparative Experiment Execution)", "BASS vs FLEX Flame Spread Analysis", [
    "[Layer 1] Data Analyst Agent: Parses user metrics (flame length: 12.4mm vs 18.2mm) -> Computes descriptive statistics & p-values",
    "[Layer 2] NASA Research Agent: Queries NTRS corpus -> Retrieves 4 BASS/FLEX papers with official URLs and page numbers [p.4, p.11]",
    "[Layer 3] Document Intelligence: Extracts experimental fuel, flow speeds (0 to 5 cm/s) and oxygen molar fractions (19% to 21%)",
    "[Layer 4] Scientific Reviewer: Audits draft answer -> Verifies each numerical claim against cited NTRS pages -> Approves verdict"
], border_color="#f59e0b")

p3 = os.path.join(output_dir, "3_agent_communication.png")
img3.save(p3)
img3.save(os.path.join(brain_dir, "3_agent_communication.png"))
print("Image 3 saved successfully")

# ==================== 4. EXECUTION FLOW ====================
img4 = Image.new("RGB", (1400, 950), color="#090d16")
d4 = ImageDraw.Draw(img4)
d4.rectangle([0, 0, 1400, 75], fill="#0f172a")
d4.text((30, 20), "IGNIS END-TO-END EXECUTION FLOW · FROM QUERY TO VERDICT", fill="#ff6b2c", font=font_title)
d4.text((1050, 26), "Query Lifecycle", fill="#64748b", font=font_sub)

stages = [
    ("STAGE 1: INGESTION", "User asks question via Streamlit UI or REST /api/ask\n• Sanitizes input string & checks token budgets (TokenManager)\n• Creates unique session tracking ID (InMemorySessionService)", "#ff6b2c"),
    ("STAGE 2: ROUTING", "Task Classifier analyzes semantic intent (orchestration/routing.py)\n• Matches keywords against 7 Workflows (A through G)\n• Determines exact sequence of specialist layers", "#3b82f6"),
    ("STAGE 3: RETRIEVAL", "Literature & NASA Data Retrieval (literature_tools.py)\n• Queries 102 NASA NTRS papers (16,168 chunks) via hybrid TF-IDF\n• Extracts verified page numbers & official NTRS URLs", "#10b981"),
    ("STAGE 4: COMPUTATION", "Deterministic Analysis & Extraction (data_tools / ml_tools)\n• Calculates descriptive stats, missing values, correlations (NumPy/Pandas)\n• Extracts conditions (pressure, O2 %, flow velocity)", "#8b5cf6"),
    ("STAGE 5: SYNTHESIS", "Multi-Agent Context Aggregation (ContextBuilder)\n• Combines specialist logs & tool outputs into running summary\n• Synthesizes draft scientific answer with inline citations [Title | NTRS URL | p.N]", "#f59e0b"),
    ("STAGE 6: REVIEW", "Scientific Reviewer Quality Gate (review_tools.py)\n• Audits claims against extracted evidence passages\n• Flags ungrounded speculation; returns final verdict (APPROVED / REVISED)", "#ef4444"),
]

for idx, (title, desc, color) in enumerate(stages):
    y = 95 + idx * 135
    d4.rounded_rectangle([40, y, 1360, y + 115], radius=10, fill="#1e293b", outline=color, width=2)
    d4.text((65, y + 15), title, fill=color, font=font_card_title)
    lines = desc.split("\n")
    curr_text_y = y + 45
    for line in lines:
        d4.text((70, curr_text_y), line, fill="#cbd5e1", font=font_body)
        curr_text_y += 24
    if idx < 5:
        arrow_y = y + 115
        d4.polygon([(700, arrow_y + 14), (690, arrow_y + 3), (710, arrow_y + 3)], fill=color)

p4 = os.path.join(output_dir, "4_execution_flow.png")
img4.save(p4)
img4.save(os.path.join(brain_dir, "4_execution_flow.png"))
print("Image 4 saved successfully")
