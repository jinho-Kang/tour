from socket import fromshare
from django import forms
from pybo.models import Question,Answer

# 모델 폼은 이너클래스인 Meta 클래스가 반드시 필요
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['subject','content']
        # 메타클래스의 widget속성을 지정하면
        # form-control과 같은 부트스트랩 클래스 추가가능
        widgets={
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control','rows':10}),
        }
        # 질문등록에서 보이게하는거 변경
        labels={
            'subject':'제목',
            'content':'내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['content']
        labels={
            'content':'답변내용',
        }