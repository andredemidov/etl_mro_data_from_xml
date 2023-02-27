from domain.entities import ObjectRepairGroup

from .get_new_data_adapter_abstract import GetNewDataAdapterAbstract


class GetNewObjectRepairGroupAdapter(GetNewDataAdapterAbstract):

    def _init_entities(self, element):
        toir_id = element.find('РеквизитыОР/ОбъектРемонта').text
        level = int(element.find('РеквизитыОР/УровеньГруппы').text)
        parent = element.find('РеквизитыОР/ОбъектРемонта_Родитель').text
        name = element.find('РеквизитыОР/ОбъектРемонтаНаименование').text
        toir_url = element.find('РеквизитыОР/СсылкаОР').text
        departament_id = element.find('РеквизитыОР/ПодразделениеВладелец').text

        repair_object = ObjectRepairGroup(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            toir_url=toir_url,
            departament_id=departament_id,
        )
        self._result_entities.append(repair_object)
