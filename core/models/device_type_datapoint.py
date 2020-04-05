from sqlalchemy.dialects.postgresql import UUID

from core.models.abstract.base_model import db
from core.models.abstract.standard_model import StandardModel


class DeviceTypeDatapoint(StandardModel):
    __tablename__ = 'device_type_datapoints'

    name = db.Column(db.String(100), nullable=True)
    units = db.Column(db.String(100), nullable=True)
    code = db.Column(db.String(100), nullable=True)
    legend = db.Column(db.String(100), nullable=True)
    writable = db.Column(db.Boolean, nullable=True)

    module_device_type_id = db.Column(UUID(as_uuid=True), db.ForeignKey('module_device_types.id'))
    module_device_type = db.relationship("ModuleDeviceType")

    def summary(self) -> dict:
        return dict(
            id=str(self.id),
            name=self.name,
            units=self.units,
            code=self.code,
            legend=self.legend,
            writable=self.writable,
            module_device_type_id=self.module_device_type.id if self.module_device_type else None
        )
