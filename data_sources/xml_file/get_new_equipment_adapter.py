from datetime import datetime
from domain.entities import Equipment

from .get_new_data_adapter_abstract import GetNewDataAdapterAbstract


class GetNewEquipmentAdapter(GetNewDataAdapterAbstract):

    def _init_entities(self, element):

        toir_id = element.find('РеквизитыОР/ОбъектРемонта').text
        level = int(element.find('РеквизитыОР/УровеньГруппы').text)
        parent = element.find('РеквизитыОР/ОбъектРемонта_Родитель').text
        name = element.find('РеквизитыОР/ОбъектРемонтаНаименование').text
        tech_number = element.find('РеквизитыОР/ТехНомер').text
        toir_url = element.find('РеквизитыОР/СсылкаОР').text
        registration_number = element.find('РеквизитыОР/РегистрационныйНомер').text
        commodity_producer = element.find('РеквизитыОР/Изготовитель').text
        commodity_number = element.find('РеквизитыОР/ЗаводскойНомер').text
        category = element.find('РеквизитыОР/КатегорияОборудования').text
        operation_date = element.find('РеквизитыОР/ДатаВводаВЭксплуатацию').text
        departament_id = element.find('РеквизитыОР/ПодразделениеВладелец').text
        object_type_id = element.find('РеквизитыОР/ТиповойОР').text
        operating = element.find('Наработка/Значение').text

        if operation_date:
            operation_date = datetime.strptime(operation_date, '%Y-%m-%dT%H:%M:%S')

        repair_object = Equipment(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            operating=operating,
            tech_number=tech_number,
            toir_url=toir_url,
            registration_number=registration_number,
            commodity_producer=commodity_producer,
            commodity_number=commodity_number,
            operation_date=operation_date,
            departament_id=departament_id,
            object_type_id=object_type_id,
            category=category,
        )
        self._result_entities.append(repair_object)
