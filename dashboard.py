from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Horizontal, Vertical

class StatPanel(Static):
    def __init__(self, label: str, value: str):
        super().__init__()
        self.label = label
        self.value = value

    def render(self) -> str:
        return f"{self.label}\n\n{self.value}"

class WeeklyChart(Static):
    def __init__(self, weekly_data: list):
        super().__init__()
        self.weekly_data = weekly_data

    def render(self) -> str:
        if not self.weekly_data:
            return "No Data"

        max_miles = max(miles for _, miles in self.weekly_data)
        bar_max = 20

        lines = []
        for week, miles in self.weekly_data:
            bar_length = int((miles / max_miles) * bar_max)
            bar = "█" * bar_length
            lines.append(f"{week} {bar:<20} {miles:.1f} mi")

        return "\n".join(lines)

class StravaApp(App):
    CSS = """
    Screen {
        background: #0f0f0f;
    }

    StatPanel {
        border: solid #333333;
        padding: 1 2;
        height: 7;
        content-align: center middle;
        width: 1fr;
    }

    #stats-row {
        height: 7;
    }
    """
    
    def __init__(self, stats: dict, weekly_data: list):
        super().__init__()
        self.stats = stats
        self.weekly_data = weekly_data

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="stats-row"):
            yield StatPanel("Yearly Mileage", self.stats.get("yearly_mileage", "-"))
            yield StatPanel("Longest Run", self.stats.get("longest_run", "-"))
            yield StatPanel("Average Pace", self.stats.get("avg_pace", "-"))
        yield WeeklyChart(self.weekly_data)
        yield Footer()

if __name__ == "__main__":
    app = StravaApp(stats={
        "yearly_mileage": "257 mi",
        "longest_run": "13.4 mi",
        "avg_pace": "11:49 /mi"
    }, weekly_data=[])
    app.run()
