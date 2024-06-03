from tira.third_party_integrations import ensure_pyterrier_is_loaded, persist_and_normalize_run
from tira.rest_api_client import Client
import pyterrier as pt

ensure_pyterrier_is_loaded()
tira = Client()

pt_dataset = pt.get_dataset('irds:ir-lab-sose-2024/ir-acl-anthology-20240504-training')

index = tira.pt.index('ir-lab-sose-2024/tira-ir-starter/Index (tira-ir-starter-pyterrier)', pt_dataset)
bm25 = pt.BatchRetrieve(index, wmodel="BM25")

print('First, we have a short look at the first three topics:')
pt_dataset.get_topics('text').head(3)

print('Now we do the retrieval...')
run = bm25(pt_dataset.get_topics('text'))
print('Done. Here are the first 10 entries of the run')
run.head(10)

persist_and_normalize_run(run, system_name='bm25-baseline', default_output='../runs')