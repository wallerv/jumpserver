# coding:utf-8
from django import forms

from .models import IDC, Asset, AssetGroup
from django.utils.translation import gettext_lazy as _


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset

        fields = [
            "ip", "other_ip", "remote_card_ip", "hostname", "port", "groups", "username", "password",
            "idc", "mac_addr", "brand", "cpu", "memory", "disk", "os", "cabinet_no", "cabinet_pos",
            "number", "status", "type", "env", "sn", "is_active", "comment"
        ]

        widgets = {
            'groups': forms.SelectMultiple(attrs={'class': 'select2', 'data-placeholder': _('Join assetgroups')}),
        }


class AssetGroupForm(forms.ModelForm):
    class Meta:
        model = AssetGroup
        fields = [
            "name", "comment"
        ]


class IdcForm(forms.ModelForm):
    class Meta:
        model = IDC
        fields = ['name', "bandwidth", "operator", 'contact', 'phone', 'address', 'network', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'network': forms.Textarea(
                attrs={'placeholder': '192.168.1.0/24\n192.168.2.0/24'})
        }
