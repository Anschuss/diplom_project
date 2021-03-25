from django.db import models
from django.utils.text import slugify


# Оборудывание

class CharacteristicsProduct(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=120, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Cleient(CharacteristicsProduct):
    pass


class Area(CharacteristicsProduct):
    img = models.ImageField(upload_to='areas', blank=True, null=True)


class Brand(CharacteristicsProduct):
    img = models.ImageField(upload_to='brands', blank=True, null=True)


class Type(CharacteristicsProduct):
    pass


class Product(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=120, unique=True, verbose_name="Название")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Область применения")
    type_product = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип")
    screen = models.ForeignKey("Screen", on_delete=models.PROTECT, verbose_name="Экран")
    weight = models.FloatField(verbose_name="Вес")
    working_conditions = models.CharField(max_length=256, verbose_name="Рабочие условия")
    storage_conditions = models.CharField(max_length=256, verbose_name="Условия хранения")
    сlients = models.ForeignKey(Cleient, on_delete=models.PROTECT, verbose_name="Наши клиенты")
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='products', blank=True, null=True)
    equipment = models.TextField()
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.brand} {self.type_product} {self.area} {self.name}')
        super(Product, self).save(*args, **kwargs)


class Consumables(models.Model):
    name = models.CharField(max_length=120, verbose_name="Название")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Область применения")
    type_product = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.brand} {self.type_product} {self.area} {self.name}')
        super(Consumables, self).save(*args, **kwargs)


class OptionalEquipment(Product):
    pass


class MassageCouch(Product):
    height = models.PositiveIntegerField(default=48)
    size = models.CharField(max_length=32)
    weight_limit = models.PositiveIntegerField(default=100)
    material = models.CharField(max_length=120)
    height_adjustment = models.BooleanField()
    electric_motor = models.BooleanField()


class Characteristics(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class TypeLibra(Characteristics):
    pass


class Units(Characteristics):
    pass


class Screen(Characteristics):
    pass


# Sports medicine


class BabyScales(Product):
    type_libra = models.ForeignKey(TypeLibra, on_delete=models.CASCADE, verbose_name="Тип")
    weight_limit = models.PositiveIntegerField(verbose_name="Максимальный вес")
    discreteness = models.PositiveIntegerField(verbose_name="Дискретность")
    cuvette = models.CharField(max_length=120, default="съёмная", verbose_name="Кювета")
    automatic = models.BooleanField(default="Есть", verbose_name="Автоматическое отключение")
    units = models.ForeignKey(Units, on_delete=models.PROTECT, verbose_name="Еденица измерения")


class Stadiometer(Product):
    measurement_parameters = models.CharField(max_length=120, verbose_name="Параметры измерения")
    measurement_range = models.CharField(max_length=120, verbose_name="Диапазон измерения роста")
    inaccuracy = models.PositiveIntegerField(verbose_name="Погрешность")
    minimum_measurement_value = models.PositiveIntegerField(verbose_name="Минимальная величина измерения")
    height_adjustment = models.PositiveIntegerField(verbose_name="Регулировка роста")
    units = models.ForeignKey(Units, on_delete=models.PROTECT, verbose_name="Единицы измерения")


class Tonometer(Product):
    power_consumption = models.FloatField(verbose_name="Потребление энергии")
    dimension = models.CharField(max_length=256, verbose_name="измерение")
    adapter = models.CharField(max_length=256, verbose_name="адаптер")
    measuring_range = models.CharField(max_length=120, verbose_name="Диапазон измерений")
    measurement_accuracy = models.CharField(max_length=120, verbose_name="Точность измерения")


class BodyCompositionAnalyzer(Product):
    pass


# Laboratory


class Сonsumables(Product):
    pass


class Immunochemistry(Product):
    pass


class BloodGasAndElectrolyteAnalyzer(Product):
    pass


class AnalysisOfUrine(Product):
    technology = models.CharField(max_length=120, verbose_name="Технология")
    performance = models.CharField(max_length=120, verbose_name="Производительность")
    lot_size = models.PositiveIntegerField(verbose_name="Объем партии")
    minimum_sample_volume = models.FloatField(verbose_name="Минимальный объем образца")
    memory_size = models.CharField(max_length=256, verbose_name="Объём памяти")
    сuvette_capacity = models.PositiveIntegerField(verbose_name="Ёмкость кюветы")


class Biochemistry(Product):
    pass


class Hematology(Product):
    pass


class Coagulometry(Product):
    analysis_methods = models.CharField(max_length=256, verbose_name="Методы анализа")
    measuring_system = models.CharField(max_length=256, verbose_name="Измерительная система")
    incubation_unit = models.CharField(max_length=256, verbose_name="Инкубационный блок")
    total_reaction_volume = models.CharField(max_length=256, verbose_name="Общий реакционный объем")
    sample_volume = models.PositiveIntegerField(verbose_name="Объем пробы")
    reagent_volume = models.PositiveIntegerField(verbose_name="Объем реагента")
    Calibration_of_tests = models.CharField(max_length=256, verbose_name="Калибровка тестов")


class ElisaDiagnostic(Product):
    sampler_capacity = models.PositiveIntegerField(verbose_name="Емкость пробоотборника")
    reagent_positions = models.PositiveIntegerField(verbose_name="Позиции реагентов")
    mtp_positions = models.PositiveIntegerField(verbose_name="Позиции MTP")
    pre_dilution_mtp_positions = models.PositiveIntegerField(verbose_name=f"Предварительное разведение \n Позиции MTP")
    dosing_volume = models.PositiveIntegerField(verbose_name="Объем дозирования")
    aspiration_volume = models.PositiveIntegerField(verbose_name="Объем аспирации")


class Electrophoresis(Product):
    pass


class ExpressDiagnostics(Product):
    system_type = models.CharField(max_length=256, verbose_name="Тип системы")
    measuring_principle = models.CharField(max_length=256, verbose_name="Принцип Измерения")
    calibration = models.CharField(max_length=256, verbose_name="Калибровка")
    combined_reagent_and_sample_carriage = models.CharField(max_length=256,
                                                            verbose_name="Комбинированная каретка для реагентов и образца")
    sample_types = models.CharField(max_length=256, verbose_name="Типы образцов")
    reagents = models.CharField(max_length=256, verbose_name="Реагенты")


# Obstetrics, Gynecology and Neonatology

class VideoColposcope(Product):
    pass


class GynecologicalChair(Product):
    pass


class IncubatorForNewborns(Product):
    pass


class FetalMonitor(Product):
    pass


class FetalDoppler(Product):
    fetal_heart_rate_range = models.CharField(max_length=256, verbose_name="диапазон значений чсс плода")
    resolution = models.CharField(max_length=32, verbose_name="разрешение")
    speaker_power = models.PositiveIntegerField(verbose_name="мощность динамика")
    signal_frequency = models.FloatField(verbose_name="частота ультразвукового сигнала")


class WarmersForNewborns(Product):
    pass


# Cosmetology


class LaserSystem(Product):
    laser_type = models.CharField(max_length=120, verbose_name="Тип лазера")
    wavelength = models.FloatField(verbose_name="Длина волны")
    laser_power = models.CharField(max_length=32, verbose_name="Мощность лазера")
    cooling_system = models.CharField(max_length=32, verbose_name="Система охлаждения")


# Neurology

class ComputerSystem(Product):
    pass


class Electroencephalograph(Product):
    pass


# Rehabilitation

class BicycleErgometer(Product):
    pass


class Treadmill(Product):
    pass


# Reanimation

class PatientMonitor(Product):
    pass


class PulseOximeter(Product):
    pass


# Radiology

class FluroscopicSystemType(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=True, null=True, verbose_name="Тип рентгеновской системы")


class FluoroscopicSystem(models.Model):
    class Meta:
        abstract = True

    type_system = models.ForeignKey(FluroscopicSystemType, on_delete=models.CASCADE,
                                    verbose_name="Тип рентгеновской системы")


class FluoroscopySystem(FluoroscopicSystem, Product):
    pass
