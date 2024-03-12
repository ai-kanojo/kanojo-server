from openai import OpenAI
import os

# client 세팅

ASSISTANT_ID='asst_TnuTyENYP7YIFjXDaVYuvEg5'

class GPTApi:
    """
    GPTApi를 통한 응답을 반환해줍니다.
    """
    def __init__(self, assistant_id=ASSISTANT_ID):
        self.client = OpenAI(api_key=os.environ['OPENAI_API_KEY']) #apikey는 알아서
        self.assistant_id = assistant_id
        self.thread = self.client.beta.threads.create()

    def send(self,message):
        """
        api에게 메시지를 보내고 받은 결과를 반환합니다.
        """
        messages = self.client.beta.threads.messages.create(
            thread_id = self.thread.id,
            role = "user",
            content = message
        )

        run = self.client.beta.threads.runs.create(
            thread_id = self.thread.id,
            assistant_id = self.assistant_id,
        )
        while True:
            if run.status == "completed":
                break

            run = self.client.beta.threads.runs.retrieve(
                thread_id = self.thread.id,
                run_id = run.id
            )

        messages = self.client.beta.threads.messages.list(
            thread_id = self.thread.id
        )

        return messages.data[0].content[0].text.value
    