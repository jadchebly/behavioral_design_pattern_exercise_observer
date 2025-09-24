class PrintNotifier:
    """Simple notifier that just prints messages."""
    def send(self, message: str) -> None:
        print(f"[Notify] {message}")
