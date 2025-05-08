from langgraph_supervisor import create_supervisor
from agents.business_analyst import analyze_business_kpis
from agents.financial_advisor import analyze_financials
from agents.market_expert import analyze_market_trends
from utils.api_utils import get_openai_model, get_google_model, get_anthropic_model

# Initialize Models
openai_model = get_openai_model()
google_model = get_google_model()
anthropic_model = get_anthropic_model()

business_analyst={"function": analyze_business_kpis, "model": "gpt-4"}
financial_advisor={"function": analyze_financials, "model": "gemini-2.0-flash"}
market_expert={"function": analyze_market_trends, "model": "claude-3-opus"}
models={"gpt-4","gemini-2.0-flash","claude-3"}
# Create Multi-Agent Supervisor
supervisor = create_supervisor(
    agents=[business_analyst,financial_advisor,market_expert],
    model=models,
    prompt=(
        "You are a supervisor managing experts for analyzing an aesthetic clinic’s business. "
        "Use Business Analyst for KPIs, Financial Advisor for financial insights, and Market Expert for trends."
    )
)


def process_query(query):
    return supervisor.run(query)
