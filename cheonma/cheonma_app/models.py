from django.db import models
import random

# Create your models here.
class Page(models.Model):
    name = models.CharField(max_length=255)

class Level(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, related_name='levels')
    level = models.IntegerField(null=True)
    effect = models.CharField(max_length=255, null=True)
    lock = models.BooleanField(default=False, null=True)
    state = models.CharField(max_length=255, null=True)

    def set_effect_and_level(self,page):
        if page == 1:
            effects = {
                1: "기본 공격 피해량",
                2: "전체 피해량",
                3: "공격 속도",
                4: "치명타 피해량",
                5: "전체 피해량",
                6: "강타 피해량",
                7: "기본 공격 피해량",
                8: "전체 피해량",
            }
        elif page == 2:
            effects = {
                1: "스킬 피해량",
                2: "전체 피해량",
                3: "기본 공격 피해량",
                4: "스킬 피해량",
                5: "받는 피해 감소",
                6: "스킬 피해량",
                7: "전체 피해량",
                8: "기본 공격 피해량",
            }
        elif page == 3:
            effects = {
                1: "체력 증가",
                2: "체력 증가",
                3: "체력 증가",
                4: "전체 피해량",
                5: "보스 피해량",
                6: "체력 증가",
                7: "체력 증가",
                8: "체력 증가",
            }
        elif page == 4:
            effects = {
                1: "내공 증가",
                2: "내공 회복 증가",
                3: "기본 공격 피해량",
                4: "치명타 피해량",
                5: "체력 증가",
                6: "이동 속도",
                7: "공격 속도",
                8: "내공 증가",
            }
        else:
            raise ValueError("Invalid page")


        if self.level in effects:
            self.effect = effects[self.level]
            self.save()
        else:
            raise ValueError("Invalid level")
        
    def set_state(self):
        probability = random.uniform(0, 100)

        if probability <= 60:
            self.state = "허술"
        elif probability <= 90:
            self.state = "기초"
        elif probability <= 97:
            self.state = "완숙"
        elif probability <= 99.5:
            self.state = "일체"
        else:
            self.state = "대성"

        self.save()

class Coin(models.Model):
    coin = models.IntegerField()