from edc_identifier.subject_identifier import SubjectIdentifier as \
    BaseSubjectIdentifier


class SubjectIdentifier(BaseSubjectIdentifier):

    template = '{protocol_number}-0{site_id}{device_id}{sequence}'


class PreFlourishIdentifier(BaseSubjectIdentifier):

    template = 'PF{protocol_number}-0{site_id}{device_id}{sequence}'
