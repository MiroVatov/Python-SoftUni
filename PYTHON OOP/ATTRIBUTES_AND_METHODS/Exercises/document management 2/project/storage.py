class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []
        self.categories_dict = {}
        self.topics_dict = {}
        self.documents_dict = {}

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)
            self.categories_dict[category.id] = category

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)
            self.topics_dict[topic.id] = topic

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)
            self.documents_dict[document.id] = document

    def edit_category(self, category_id: int, new_name:str):
        # Version - 1
        # for category in self.categories:
        #     if category.id == category_id and category.name != new_name:
        #         category.name = new_name

        category = [category for category in self.categories if category.id == category_id and category.name != new_name]
        if category:
            category[0].name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):

        # Version - 1
        # for topic in self.topics:
        #     if topic.id == topic_id:
        #         if topic.topic != new_topic:
        #             topic.topic = new_topic
        #         if topic.storage_folder != new_storage_folder:
        #             topic.storage_folder = new_storage_folder

        topic = [topic for topic in self.topics if topic.id == topic_id and topic.storage_folder != new_storage_folder]
        if topic:
            topic[0].storage_folder = new_storage_folder
            topic[0].topic = new_topic

    def edit_document(self, document_id: int, new_file_name: str):

        # Version - 1
        # for document in self.documents:
        #     if document.id == document_id and document.file_name != new_file_name:
        #         document.file_name = new_file_name

        document = [document for document in self.documents if document.id == document_id and document.file_name != new_file_name]
        if document:
            document[0].file_name = new_file_name

    def delete_category(self, category_id):

        for category in self.categories:
            if category_id == category.id:
                self.categories.remove(category)

    def delete_topic(self, topic_id):

        for topic in self.topics:
            if topic.id == topic_id:
                self.topics.remove(topic)

    def delete_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                self.documents.remove(doc)

    def get_document(self, document_id):
        if document_id in self.documents_dict.keys():
            return self.documents_dict[document_id]

    def __repr__(self):
        data = ''
        for document in self.documents:
            data += f"{document.__repr__()}" + '\n'
            return data

