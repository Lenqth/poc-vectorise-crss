# Vectorise PoC for crss.gnknzm.net

https://github.com/gnknzm/crss.gnknzm.net

において、ダジャレの重複を見つけるために、ベクトル化をやってみる


## make vectors.json

```
python ./make_vector.py ./crss.json
```

## search from vectors.json

```
python ./search.py "未成年にはみせんねん"
```

```
[{'id': 'CRE-2024-36426', 'metadata': {'author': 'RyotaK', 'vector_string': 'CRSS:1.0/SI:H/GC:M/UK:M/TL:N/CA:L'}, 'page_content': '未成年にはみせへんねん', 'type': 'Document', 'similarity': 0.9853977885869423}, {'id': 'CRE-2024-36427', 'metadata': {'author': 'RyotaK', 'vector_string': 'CRSS:1.0/SI:H/GC:H/UK:L/TL:N/CA:L'}, 'page_content': '未成年には見せんねん', 'type': 'Document', 'similarity': 0.9215695161166202}, {'id': 'CRE-2025-47022', 'metadata': {'author': 'Lenqth', 'vector_string': 'CRSS:1.0/SI:H/GC:H/UK:L/TL:N/CA:L'}, 'page_content': '新年なにしてんねん', 'type': 'Document', 'similarity': 0.8728533714798029}, {'id': 'CRE-2025-47000', 'metadata': {'author': 'RyotaK', 'vector_string': 'CRSS:1.0/SI:H/GC:M/UK:L/TL:N/CA:L'}, 'page_content': '"新年" そうそうオヤジギャグなんて言ったら "因縁" つけられちまうよ', 'type': 'Document', 'similarity': 0.8221718746316679}]

```