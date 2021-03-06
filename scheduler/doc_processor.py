# -*- coding: utf-8 -*-
import docx
from show import Show, ShowEncoder
import json


class DocumentProcessor(object):
    def __init__(self):
        pass

    def get_shows(self, doc_path):
        doc = docx.Document(doc_path)
        table = doc.tables[0]

        # Get the column indices
        indices = dict()

        i = 0
        while i < len(table.columns):
            if table.columns[i].cells[0].text == u'NO.':
                indices['number'] = i
            if table.columns[i].cells[0].text == u'时间':
                indices['plan'] = i
            if table.columns[i].cells[0].text == u'时长':
                indices['duration'] = i
            if table.columns[i].cells[0].text == u'节目':
                indices['name'] = i
            i += 1

        # Get the raw data
        i = 1
        shows = []
        while i < len(table.rows):
            row = table.rows[i]
            seq = str(i)
            name = row.cells[indices['name']].text
            duration = row.cells[indices['duration']].text
            plan = row.cells[indices['plan']].text
            # print ','.join([seq, name, duration, plan])
            shows.append(Show({'number': seq, 'name': name, 'duration': duration, 'plan': plan}))
            i += 1

        return json.dumps(shows, cls=ShowEncoder)


if __name__ == '__main__':
    doc_path = 'uploads/data.docx'
    processor = DocumentProcessor()
    shows = processor.get_shows(doc_path)
    print shows
