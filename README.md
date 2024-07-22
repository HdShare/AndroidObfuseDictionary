# Android混淆字典

## 说明:

使用乱码方块混淆包名,类名,方法名,变量名等

```
ᛱ ᛲ ᛳ ᛴ ᛵ ᛶ ᛷ ᛸ ᤝ ᤞ ᲀ ᲁ ᲇ ᲈ
```

## 用法:

在proguard-rules.pro中添加以下配置

```
-obfuscationdictionary obf-dict.txt
-classobfuscationdictionary obf-dict.txt
-packageobfuscationdictionary obf-dict.txt
```
