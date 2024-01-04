from datetime import datetime
from django.test import Client, TestCase

from polls.models import Question

# Create your tests here.


class IndexTestCase(TestCase):
    def setUp(self):
        # ここに前テストケースで共通の下準備を書く
        # Questionを2つ作成
        self.question1 = Question.objects.create(
            question_text="Test First Question?",
            pub_date=datetime.now()
        )

        self.question2 = Question.objects.create(
            question_text="Test Second Question?",
            pub_date=datetime.now()
        )

    # Question一覧表示
    def test_show_question_list(self):

        # HTTPリクエストクライアントを作成
        client = Client()

        response = client.get("/polls/")

        # HTML内にQuestionモデルインスタンスの文字列が含まれている
        self.assertContains(response, "Test First Question?", html=True)
        self.assertContains(response, "Test Second Question?", html=True)

        # レスポンスで取得したコンテキスト内のモデルが存在する
        self.assertEqual(
            response.context['latest_question_list'][1],
            self.question1
        )
        self.assertEqual(
            response.context['latest_question_list'][0],
            self.question2
        )
