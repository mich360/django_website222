from typing import Any, Dict
from django. views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "大谷"
        return ctxt

class AboutView(TemplateView):   #aboutページ追加する
    template_name = "about.html"   

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"] = 123456789
        ctxt["skills"] = [
            "1994年7月5日に生まれ、身長は約190cm、体重は約94kgです。",
            "2012年には第94回全国高校野球選手権大会で優勝",
            "2013年のプロ野球ドラフト会議で、ロッテオリオンズから1位指名",
            "2016年にはリーグ最多勝を獲得し、最優秀防御率、最多奪三振のタイトルも獲得",
            "2017年には、アメリカのメジャーリーグベースボール（MLB）のロサンゼルス・エンゼルスに移籍",
            "二刀流として投手と打者の両方の能力",
        ]
        return ctxt     


