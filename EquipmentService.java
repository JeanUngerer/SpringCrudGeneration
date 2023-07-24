package com.oldhammer.fantasylistbuilder.services;

import com.oldhammer.fantasylistbuilder.DTOs.EquipmentDTO;
import com.oldhammer.fantasylistbuilder.exception.ExceptionHandler;
import com.oldhammer.fantasylistbuilder.helpers.CycleAvoidingMappingContext;
import com.oldhammer.fantasylistbuilder.mappers.EquipmentMapper;
import com.oldhammer.fantasylistbuilder.models.Equipment;
import com.oldhammer.fantasylistbuilder.repositories.EquipmentRepository;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import lombok.extern.log4j.Log4j2;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
@Log4j2
@Transactional
public class EquipmentService {

	EquipmentRepository equipmenRepository;

	EquipmentMapper equipmenMapper;

	public List<Equipment> findAllEquipment() {
		try {
			log.info("findAllEquipment");
			List<Equipment> equipmenList = new ArrayList<Equipment>();
			equipmenRepository.findAll().forEach(ct -> equipmenList.add(equipmenMapper.entityToModel(ct)));
			return equipmenList;
		} catch (Exception e) {
			log.error("We could not find all equipmen: " + e.getMessage());
			throw new ExceptionHandler("We could not find your equipmens");
		}
	}

	public Equipment findEquipmentById(Long id) {
		try {
			log.info("findEquipmentById - id: " + id.toString());
			Equipment equipmen = equipmenMapper.entityToModel(equipmenRepository.findById(id).orElseThrow(()
				-> new ExceptionHandler("We didn't find your equipmen")));
			return equipmen;
		} catch (Exception e) {
			log.error("We could not find all equipmen: " + e.getMessage());
			throw new ExceptionHandler("We could not find your equipmen");
		}
	}

	public Equipment createEquipment(EquipmentDTO dto) {
		try {
			log.info("createEquipment");
			Equipment equipmen = equipmenMapper.dtoToModel(dto);
			equipmenRepository.save(equipmenMapper.modelToEntity(equipmen));
			return equipmen;
		} catch (Exception e) {
			log.error("Couldn't equipmen user: " + e.getMessage());
			throw new ExceptionHandler("We could not create your equipmen");
		}
	}

	public Equipment updateEquipment(EquipmentDTO dto) {
		try {
			log.info("updateEquipment - id: " + dto.getId().toString());
			Equipment equipmen = equipmenMapper.entityToModel(equipmenRepository.findById(dto.getId()).orElseThrow(()
				-> new ExceptionHandler("We could not find your equipmen")));
			equipmenMapper.updateFromDto(dto, equipmen, new CycleAvoidingMappingContext());
			equipmenRepository.save(equipmenMapper.modelToEntity(equipmen));
			return equipmen;
		} catch (Exception e) {
			log.error("Couldn't update user: " + e.getMessage());
			throw new ExceptionHandler("We could not update your equipmen");
		}
	}

	public String deleteEquipment(Long id) {
		try {
			log.info("deleteEquipment - id: " + id.toString());
			Equipment equipmen = equipmenMapper.entityToModel(equipmenRepository.findById(id).orElseThrow(()
				-> new ExceptionHandler("We could not find your equipmen")));
			equipmenRepository.delete(equipmenMapper.modelToEntity(equipmen));
			return "Equipment deleted";
		} catch (Exception e) {
			log.error("Couldn't delete equipmen: " + e.getMessage());
			throw new ExceptionHandler("We could not delete your equipmen");
		}
	}
}
