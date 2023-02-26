# -*- coding: utf-8 -*-
# Script: Definition of all messages for german localization
#
# PLEASE NOTE that this file is part of the GOM Inspect Professional software
# You are not allowed to distribute this file to a third party without written notice.
#
# Copyright (c) 2016 GOM GmbH
# Author: GOM Software Development Team (M.K.)
# All rights reserved.

# GOM-Script-Version: 8.1
#
# ChangeLog:
# 2015-07-01: Initial Creation (Based on solution by M.G./GOM Süd)


from KioskInterface.Base.Misc import Messages


class Localization( Messages.Localization ):

	######################################################
	### Deutsche Benutzeroberfläche für Standard-Kiosk ###
	######################################################

	### Hinweis: ############################################################################
	### Die Variablen-Namen (z.B.: startdialog_label_title) dürfen nicht geändert werden! ###
	#########################################################################################

	# Allgemein
	msg_general_failure_title = 'Fehler'
	msg_global_failure_text = 'Unerwarteter Fehler: '

	# Status-Meldungen: PROGRESSDIALOG
	msg_evaluate_process_text = 'Prozessschritt: {0} von {1}'
	msg_evaluate_detail_msg_initialize = 'Voreinstellungen laden'
	msg_evaluate_detail_msg_reports = 'Reportseiten werden aktualisiert'
	msg_evaluate_detail_msg_recalc = 'Neuberechnung des Projektes'
	msg_evaluate_detail_msg_polygonize = 'Polygonisierung'
	msg_evaluate_detail_msg_photogrammetry = 'Photogrammetrie'
	msg_evaluate_detail_msg_digitizing = 'Digitalisierung'
	msg_evaluate_detail_msg_safety_home = 'Sicher zur Home-Position zurückkehren'
	msg_evaluate_detail_calibrate = 'Kalibrierung'
	msg_evaluate_estimated_time = 'Geschätzte verbleibende Messzeit: {} Minuten'

	# Asyncron-Modus
	msg_async_failure_title = 'Kommunikationsfehler'
	msg_async_failure_start_server = 'Start des Kommunikations-Server fehlgeschlagen'
	msg_async_failure_communicate_client = 'Kommunikation über den Async-Client fehlgeschlagen'
	msg_async_client_process_working = 'Projektverarbeitung {}'
	msg_async_client_process_finished = 'Projekt abgeschlossen {}'
	msg_async_client_result = 'Teile-Nr {0}: {1} Elemente überprüft, {2} Elemente nicht berechnet und {3} Elemente ausserhalb der Toleranz'

	# Status und Fehlermeldungen
	msg_system_configuration_failed_title = 'Systemkonfiguration wird überprüft'
	msg_no_measurement_list = 'Keine kompatible Messreihe in der Vorlage'
	msg_no_measurement_list_real = '<b>Verbundene Hardware:</b>'
	msg_calibration_failed_execute = 'Kalibrier-Messreihe konnte nicht durchgeführt werden.'
	msg_calibration_no_list_defined = 'Keine Kalibrier-Messreihe definiert'
	msg_photogrammetry_no_list_defined = 'Keine Photogrammetrie-Messreihe definiert'
	msg_photogrammetry_verification_failed = 'Überprüfung der Photogrammetrie-Messreihe fehlgeschlagen.'
	msg_photogrammetry_failed_execute = 'Photogrammetrie-Messreihe konnte nicht durchgeführt werden'
	msg_digitizing_no_list_defined = 'Keine Digitalisierungs-Messreihe definiert'
	msg_digitizing_failed_execute = 'Messreihe konnte nicht durchgeführt werden'
	msg_digitizing_failed_maxrepetitions = 'Digitalisierungs-Messreihe konnte nicht durchgeführt werden'
	msg_digitizing_failed_already_calibrated = 'Digitalisierungs-Messreihe konnte nicht durchgeführt werden.<br/>Die Kalibrier-Messreihe wurde bereits durchgeführt.'
	msg_sensor_failed_init = 'Sensor-Initialisierung fehlgeschlagen'
	msg_sensor_failed_warmup = 'Während der Sensoraufwärmzeit ist ein Fehler aufgetreten'
	msg_msetup_sensor_offline = 'Sensor ist nicht initialisiert'
	msg_msetup_define_active_failed = 'Messaufbau konnte nicht aktiviert werden'
	msg_safely_move_failed = 'Die Home-Position konnte nicht sicher angefahren werden'
	msg_sensor_warning = 'ATOS ScanBox Warnung:<br/>{}'
	msg_evaluate_failed_home_check_series = 'Die Auswertung wurde abgebrochen,da keine Home-Position<br/>am Beginn und am Ende der Messreihe definiert wurde'
	msg_calibration_too_often = 'Kalibrierung wurde bereits durchgeführt<br/>Nächste mögliche Kalibration in {}'
	msg_userabort = 'Benutzerabbruch'
	msg_verification_failed = 'Bei der Überprüfung der Messung ist ein Fehler aufgetreten'
	msg_verification_transformation_exception = 'Abbruch wegen eines Transformationsfehlers.'
	msg_verification_temperature_exception = 'Abbruch wegen eines Temperaturdifferenzfehlers.'
	msg_verification_move_light_exception = 'Abbruch wegen eines Verfahr- oder Belichtungsfehlers.'
	msg_verification_scale_bar_identify = 'Die Maßstäbe konnten nicht gefunden werden'
	msg_verification_no_scan_data = 'Keine Messreihe mit Scandaten vorhanden'
	msg_verification_refpointmismatch = 'Das Ausrichtung-Residuum wurde überschritten.<br/>Die Photogrammetrie passt nicht zur Digitalisierung!'
	msg_emergency_button = 'Der Not-Aus-Schalter wurde betätigt.'
	msg_multi_comprehensive_retries_exceeded = 'Die maximale Anzahl der Wiederholungen<br/>für die globale Photogrammetrie wurde überschritten.'
	msg_reverse_move_not_allowed = 'Nach Not-Aus: Diese Anlage erlaubt kein Rückwärtsfahren in die Home-Position.'
	msg_no_points_for_trafo = 'Es konnten nicht genügend kodierte Punkte für die Transformation über gemeinsame Referenzpunkte gefunden werden.'

	# Überprüfungsmeldung
	msg_verification_transformation_failed = 'Transformationslimit wurde in {0} Messungen überschritten.<br/>Nur {1} sind zugelassen.'
	msg_verification_projector_residual_failed = 'Projektor-Residuum wurde in {0} Messungen überschritten.<br/>Nur {1} sind zugelassen.'
	msg_verification_movement_check_failed = 'Die Bewegungskontrolle wurde in {0} Messungen überschritten.'
	msg_verification_lighting_failed = 'Die Belichtungskontrolle wurde in {0} Messungen überschritten.'
	msg_verification_intersection_failed = 'Die Einschneide-Abweichung wurde in {0} Messungen überschritten.'
	msg_verification_global_digitize_failed = 'Die Überprüfung der Ausrichtung ist fehlgeschlagen'
	msg_verification_global_digitize_too_large = 'Das Ausrichtungs-Residuum ist zu groß.'
	msg_verification_unrecoverable_position = 'Eine ungültige Roboter-Position wurde gefunden'
	msg_verification_calibration_failed = 'Überprüfung der Kalibrierung fehlgeschlagen.'

	msg_fixture_position_check_title = 'Überprüfe Messaufnahme Position.'
	msg_fixture_position_check_failed = 'Position ist nicht richtig, korrigieren Sie den Aufbau und versuchen Sie es erneut.'
	msg_fixture_position_check_failed_component_not_found = 'Nicht alle Punktkomponenten konnten identifiziert werden.' #'Not all point components could be identified.'
	msg_fixture_position_check_failed_missing_points = 'Es wurden nicht genug Punkte gefunden.' #'Not enough points were found.'
	msg_fixture_position_check_failed_rotated = 'Der Aufbau ist verdreht.' #'The part is rotated.'
	msg_fixture_position_check_failed_position = 'Der Aufbau ist verschoben.' #'The part is positioned incorrectly.'
	msg_fixture_position_check_not_performed = 'Die Positionsprüfung der Messaufnahme wurde nicht durchgeführt!<br/>.Die Vorlage enthält nicht alle benötigten Elemente.<br/>Bitte überprüfen Sie ob der Aufbau korrekt ist!'

	# Startdialog - Singlepart: STARTDIALOG_FIXTURE
	startdialog_label_title = '<p style="font-size: 48px">Willkommen</p>'
	startdialog_label_part = 'Teil "{}"'
	startdialog_label_user = 'Benutzer:'
	startdialog_label_serial = 'Seriennummer:'
	startdialog_label_batch = 'Chargennummer:'
	startdialog_label_fixture = 'Vorrichtung:'
	startdialog_label_template = 'Vorlage:'
	startdialog_button_template = 'Auswählen'
	startdialog_button_start = 'Start'
	startdialog_button_exit = 'Beenden'
	startdialog_button_next = 'Vor'
	startdialog_button_prev = 'Zurück'

	# Startdialog - Multipart : MULTIPART_WIZARD
	multipart_wizard_button_next = 'Vor'
	multipart_wizard_button_prev = 'Zurück'
	multipart_wizard_label_title = '<p style="font-size: 32px">Geben Sie die Seriennummern ein<br> und wählen Sie die Vorlagen</p>'
	multipart_wizard_label_page = 'Seite {} von {}'
	multipart_waitdialog_title = '<p align="center">Messaufbau an die Vorlage anpassen<br/>{}</p>'
	multipart_waitdialog_button_ok = 'OK'
	multipart_waitdialog_button_cancel = 'Abbrechen'

	# Progressdialog: PROGRESSDIALOG
	progessdialog_label_title = 'Messprozess wird durchgeführt'
	progressdialog_multipart_label = 'Anzahl der Projekte'

	# Bestätigungsdialog: CONFIRMDIALOG
	confirmdialog_label_title = '<p style="font-size: 48px">Messung übernehmen</p>'
	confirmdialog_label_instruction = '<p style="font-size: 32px">Akzeptieren Sie die Messung?</p>'
	confirmdialog_button_approve = 'Akzeptieren'
	confirmdialog_button_reject = 'Verwerfen'

	# Fehlermeldungsdialog: ERRORMSG_DIALOG
	errordialog_button_retry = 'Wiederholen'
	errordialog_button_abort = 'Abbrechen'
	errordialog_button_close = 'Schliessen'
	errordialog_button_gomsic = 'GOMSic'
	errordialog_button_continue = 'Fortsetzen'

	# Warten Dialog
	waitdialog_title = 'Bitte warten...'
	waitdialog_client_setup = 'Clients werden konfiguriert...'
	waitdialog_clients_exit = 'Auf Beendigung der Clients warten...'

	# Sonstige Meldungen
	measuring_setup_title = '<p align="center">Stellen Sie sicher, dass der Messaufbau<br/>für die Messreihe eingerichtet ist:</p>'
	measuring_setup_button_ok = 'OK'
	measuring_setup_button_cancel = 'Abbrechen'
	temperature_title = '<p align="center" style="font-size: 32px">Geben Sie die aktuelle Temperatur ein (in °C)</p>'
	temperature_button_ok = 'OK'
	temperature_button_cancel = 'Abbrechen'
	msg_common_refpoint_trafo_less_points = 'Die Ausrichtung über gemeinsame Referenzpunkte ist fehlgeschlagen:<br/>Weniger als drei Punkte gefunden!'
	msg_common_refpoint_trafo_error = 'Die Ausrichtung über gemeinsame Referenzpunkte ist fehlgeschlagen: {}'

	msg_cannot_execute = 'Die Auswertung des Projektes konnte nicht durchgeführt werden:<br/>Kein VMR vorhanden, oder nicht alle Messungen haben geprüfte Pfade!'

	msg_settings_errortitle = 'Kiosk Einstellungsfehler'
	msg_setting_invalid = 'Unerwarteter Fehler: ungültige Einstellung {}'
	msg_settings_savepath_failed = 'Es konnte nicht auf den Speicherpfad zugegriffen werden "{}"<br/>Bitte kontaktieren Sie Ihren Administrator und starten Sie das Setup-Skript in der Skript-Sammlung'
	msg_settings_idrange_failed = 'Interpretation der Einstellung "PhotogrammetryCodedPointIDRange" fehlgeschlaten: "{}"<br/>Bitte korrigieren Sie den Wert in der Kiosk-Konfigurationsdatei'
	msg_settings_comprehensive_batchscan = '"PhotogrammetryComprehensive" ist nur im BatchScan-Modus benutzbar.'
	msg_settings_comprehensive_independent = '"PhotogrammetryComprehensive" und "PhotogrammetryIndependent" können nicht gleichzeitig aktiviert werden.'
	msg_settings_secondary_paths = '"DoubleRobot_ClientSavePath" und "DoubleRobot_ClientTransferPath" müssen unterschiedlich sein.'
	msg_settings_aligniter_nomlist = '"AlignmentIteration" setzt "MSeriesSelection = True" voraus.'
	msg_settings_repetition_value = 'Der Minimalwert von "MaxDigitizeRepetition" ist 1 (1 Messung und keine Wiederholung).'
	msg_settings_failmargin_value = '"MeasurementFailureMargin" erlaubt nur Werte zwischen 0.0 und 1.0.'
	msg_settings_inline_ioextension = '"Inline" und "IOExtension" kann nicht gleichzeitig aktiv sein.'

	msg_platform_not_supported = 'Es wird nur die Window-Plattform unterstützt!'
	msg_only_with_atos_onlinemode = 'Nur die ATOS Software unterstützt den Online-Modus!'

	msg_barcode_connectionfailed = 'Verbindung mit dem Barcode-Scanner konnte nicht hergestellt werden<br/>Port COM{}'

	msg_disc_space_warning = 'Speicherplatzwarnungs Grenze erreicht!<br/>Noch {}MB frei auf {}'
	msg_disc_space_error = 'Speicherplatzfehler Grenze erreicht!<br/>Noch {}MB frei auf {}'
	msg_save_error_title = 'Endgültige Speicherung des Projektes fehlgeschlagen'
	msg_save_error_message = 'Ungenügender Festplattenplatz für das ausgewertete Projekt.'

	project_consistency_title = 'Ungültige Projekt-Vorlage'
	project_consistency_report_alignments = '<b>Ausrichtungen in Reports:</b>'
	project_consistency_required_alignments = '<b>Erforderliche Ausrichtungen:</b>'
	project_consistency_vmr = '<b>VMR:</b>'
	project_consistency_measuring_setups = '<b>Messaufbauten:</b>'
	project_consistency_computation_status = '<b>Berechnungsstatus:</b>'
	project_consistency_path_status = '<b>Pfadstatus:</b>'
	project_consistency_vmr_measurement_series = '<b>VMR-Messreihen:</b>'
	project_consistency_report_status = '<b>Reportstatus:</b>'
	project_consistency_measurement_status = '<b>Messungsparameter:</b>'
	project_consistency_photogrammetry = '<b>Photogrammetrie:</b>'
	project_consistency_nco = '<b>Elemente in der Zwischenablage:</b>'
	project_consistency_preview_mode = '<b>Projekt:</b>'
	project_consistency_non_master_actual_data = '<b>Elemente mit Ist-Daten werden beibehalten:</b>'
	project_consistency_2_indep_tritops = 'Mehr als eine unabhängige Photogrammetrie in einem Messaufbau'

	# Standard Keywords Beschreibungen
	keyword_description_user = 'Prüfer'
	keyword_description_serial = 'Teile-Nr.'
	keyword_description_fixture = 'Vorrichtungsnr.'
	keyword_description_date = 'Datum'

	# Statusleiste
	statusbar_text_multipart_progress = '<center>Ausführung der Messung {} von {}</center>'

	# ATOS Inline
	msg_no_atos_inline_license = 'ATOS Inline Lizenz wird benötigt!'

	# Doppelroboter Kiosk Meldungen
	msg_DC_client_failure = 'Fehler Secondary-Seite: {}'
	msg_DC_temperature_error_title = 'Fehler Temperatur Voreinstellungen'
	msg_DC_temperature_error_text = 'In den ATOS Voreinstellungen ist die Temperaturerfassungsmethode auf "Benutzer fragen" eingestellt.<br/>Doppelroboteranlagen können nur mit den Einstellungen "Feste Raumtemperatur" oder "Thermometer der Anlage" betrieben werden. Bitte korrigieren Sie die ATOS Voreinstellungen.'
	dialog_DC_ms_title = 'Welche Messreihen sollen ausgeführt werden?'
	dialog_DC_ms_text = 'Welche Messreihen sollen während\ndes Messvorganges ausgeführt werden?'
	dialog_DC_ms_align = 'Welche Messreihe soll\nfür den Einstellprozess benutzt werden?'
	dialog_DC_ms_all_untagged = 'Alle Messreihen ohne Tags'
	dialog_DC_ms_all = 'Alle Messreihen'
	dialog_DC_ms_start = 'Start'
	dialog_DC_ms_abort = 'Abbrechen'
	msg_DC_no_slave_mlist_found = 'Keine entsprechende Messreihe auf der Secondary-Seite gefunden'
	status_DC_choose_measurements = 'Bitte wählen Sie eine Messreihe'
	msg_DC_refcubes_not_unique = 'Die Vorlage enthält mehr als ein Referenzwürfel Element. Die Prüfung der Referenzwürfel wird nicht ausgeführt.'
	msg_DC_no_refcubes = 'Die Vorlage verwendet die Robogrammetrie Arbeitsweise, enthält aber keine simulierten Referenzwürfel.'
	msg_DC_refcubes_failed = 'Prüfung der Referenzwürfel fehlgeschlagen.'
	msg_DC_refcube_check_retry = 'Die Referenzwürfel "Verwenden" wie sie sind oder ihre Positionen "Korrigieren"?'

	dialog_DC_RefCube_ask_use = 'Verwenden'
	dialog_DC_RefCube_ask_retry = 'Korrigieren'
	dialog_DC_RefCube_ask_abort = 'Abbrechen'
	dialog_DC_RefCube_template_use = 'Fortsetzen'

	msg_DC_slave_failed_open = '{} - Öffnen der Vorlage fehlgeschlagen'
	msg_DC_slave_drivefull = '{} - Grenze Speicherplatz erreicht'
	msg_DC_slave_invalid_project = '{} - Ungültiges Projekt'

	msg_DC_slave_measurement_series_not_found = '{} - Messreihe nicht gefunden'
	msg_DC_slave_failed_to_copy = '{} - Fehler beim Kopieren der Messdatei auf {}\n{}'

	dialog_mlist_ask_use = 'Verwenden'
	dialog_mlist_ask_retry = 'Wiederholen'
	dialog_mlist_ask_abort = 'Abbrechen'
	msg_mlist_retry = 'Soll die Messreihe erneut ausgeführt werden?'

	dialog_oneshot_ask_clear = 'Messdaten löschen'
	dialog_oneshot_ask_keep = 'Messdaten beibehalten'
	dialog_oneshot_ask_abort = 'Abbrechen'
	dialog_oneshot = 'Das geöffnete Projekt wird im Doppelroboter Modus ausgeführt. Wollen Sie die Messdaten beibehalten oder vor der Ausführung löschen?'
	msg_oneshot_export_error = 'Der Export des temporären Projektes ist auf der Secondary-Seite fehlgeschlagen.'
