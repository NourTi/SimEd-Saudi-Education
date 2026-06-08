"""
Slack connector for SimEd Studio Bot
"""

from core.agent import SimEdAgent
from slack_sdk import WebClient
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest
from slack_sdk.socket_mode.response import SocketModeResponse


class SlackBot:
    def __init__(self, bot_token: str, app_token: str):
        self.client = WebClient(token=bot_token)
        self.socket_client = SocketModeClient(
            app_token=app_token, web_client=self.client
        )
        self.agent = SimEdAgent()

    def handle_events(self, ack, body):
        """Handle Slack events"""
        ack()

        if body["type"] == "app_mention":
            self._handle_mention(body)
        elif body["type"] == "message" and "thread_ts" not in body:
            self._handle_dm(body)

    def _handle_mention(self, body):
        """Handle mentions"""
        text = body["event"]["text"]
        user_id = body["event"]["user"]
        channel = body["event"]["channel"]

        if "start" in text.lower():
            response = self.agent.start_conversation(user_id)
        else:
            response = self.agent.process_message(user_id, text)

        self.client.chat_postMessage(channel=channel, text=response)

    def _handle_dm(self, body):
        """Handle direct messages"""
        text = body["event"]["text"]
        user_id = body["event"]["user"]
        channel = body["event"]["channel"]

        response = self.agent.process_message(user_id, text)
        self.client.chat_postMessage(channel=channel, text=response)

    def start(self):
        """Start Slack bot"""
        self.socket_client.socket_connect()
        print("✅ Slack bot connected")
        self.socket_client.start()


def run_slack(bot_token: str, app_token: str):
    """Start Slack bot"""
    bot = SlackBot(bot_token, app_token)
    bot.start()
