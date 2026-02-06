from django.db import models


class ChatHistory(models.Model):
    """AI聊天历史记录"""
    userid = models.BigIntegerField(verbose_name='用户ID')
    question = models.TextField(verbose_name='用户问题')
    answer = models.TextField(verbose_name='AI回答')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'chat_history'
        verbose_name = 'AI聊天历史'
        verbose_name_plural = verbose_name
        ordering = ['-addtime']

    def __str__(self):
        return f"User {self.userid}: {self.question[:50]}"
