from agentverse.knowledge_base.kb_doc_api import search_docs
from agentverse.knowledge_base.kb_service.base import KBServiceFactory
from agentverse.utils import BaseResponse


def kb_chat_test():
    knowledge_base_name = "samples"
    query = "什么是角色提示技术？"
    top_k = 5
    score_threshold = 0.8
    kb = KBServiceFactory.get_service_by_name(knowledge_base_name)
    if kb is None:
        return BaseResponse(code=404, msg=f"未找到知识库 {knowledge_base_name}")

    docs = search_docs(query, knowledge_base_name, top_k, score_threshold)
    context = "\n".join([doc.page_content for doc in docs])
    print("query:", query)
    print("context:", context)


if __name__ == "__main__":
    kb_chat_test()