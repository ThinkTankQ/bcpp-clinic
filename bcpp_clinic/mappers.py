from edc_map.site_mappers import site_mappers

from edc_map.mapper import Mapper


class BotswanaPlotMapper(Mapper):

    map_area = 'botswana'
    map_code = '00'
    pair = 0
    regions = []
    sections = []
    intervention = False
    landmarks = []
    center_lat = -22.543839
    center_lon = 23.855027
    radius = 900


site_mappers.register(BotswanaPlotMapper)


class AnonymousMapper(Mapper):

    map_area = 'austin'
    map_code = '88'
    center_lat = -30.2671500
    center_lon = 97.7430600
    radius = 100.5
    location_boundary = ()
    intervention = True
    landmarks = None


site_mappers.register(AnonymousMapper)


class TestPlotMapper(Mapper):

    map_area = 'test_community'
    map_code = '01'
    pair = 0
    landmarks = ()
    center_lat = -24.557709
    center_lon = 25.807963
    clinic_lat = -24.645541
    clinic_lon = 25.912407
    radius = 100.5
    location_boundary = ()
    intervention = True


site_mappers.register(TestPlotMapper)


class BokaaPlotMapper(Mapper):

    map_area = 'bokaa'
    map_code = '17'
    pair = 4
    intervention = False
    landmarks = None
    center_lat = -24.426910
    center_lon = 26.020618
    radius = 5.5


site_mappers.register(BokaaPlotMapper)


class DigawanaPlotMapper(Mapper):

    map_area = 'digawana'
    map_code = '12'
    pair = 1
    center_lat = -25.330451
    center_lon = 25.556502
    radius = 3.5
    landmarks = None
    intervention = True


site_mappers.register(DigawanaPlotMapper)


class GumarePlotMapper(Mapper):

    map_area = 'gumare'
    map_code = '35'
    pair = 13
    intervention = True
    landmarks = None
    center_lat = -19.362483
    center_lon = 22.165860
    radius = 5.5


site_mappers.register(GumarePlotMapper)


class GwetaPlotMapper(Mapper):

    map_area = 'gweta'
    map_code = '34'
    pair = 12
    intervention = True
    landmarks = None
    center_lat = -20.205298
    center_lon = 25.250788
    radius = 5.5


site_mappers.register(GwetaPlotMapper)


class LentsweletauPlotMapper(Mapper):

    map_area = 'lentsweletau'
    map_code = '16'
    pair = 3
    center_lat = -24.253009
    center_lon = 25.853233
    radius = 5.0
    intervention = True
    landmarks = None


site_mappers.register(LentsweletauPlotMapper)


class LeralaPlotMapper(Mapper):

    map_area = 'lerala'
    map_code = '21'
    pair = 6
    intervention = True
    landmarks = None
    center_lat = -22.781363
    center_lon = 27.760241
    radius = 5.5


site_mappers.register(LeralaPlotMapper)


class LetlhakengPlotMapper(Mapper):

    map_area = 'letlhakeng'
    map_code = '15'
    pair = 3
    landmarks = None
    center_lat = -24.099945
    center_lon = 25.033250
    radius = 5.0
    intervention = False


site_mappers.register(LetlhakengPlotMapper)


class MasungaPlotMapper(Mapper):

    map_area = 'masunga'
    map_code = '37'
    pair = 15
    intervention = True
    landmarks = None
    center_lat = -20.667218
    center_lon = 27.428340
    radius = 7.5


site_mappers.register(MasungaPlotMapper)


class MathangwanePlotMapper(Mapper):

    map_area = 'mathangwane'
    map_code = '31'
    pair = 11
    intervention = True
    landmarks = None
    center_lat = -20.993214
    center_lon = 27.333963
    radius = 6.5


site_mappers.register(MathangwanePlotMapper)


class MaunatlalaPlotMapper(Mapper):

    map_area = 'maunatlala'
    map_code = '23'
    pair = 7
    intervention = True
    landmarks = None
    center_lat = -22.8658437618
    center_lon = 27.4198811366
    radius = 5.5


site_mappers.register(MaunatlalaPlotMapper)


class MetsimotlhabePlotMapper(Mapper):

    map_area = 'metsimotlhabe'
    map_code = '29'
    pair = 9
    intervention = False
    landmarks = None
    center_lat = -24.554426
    center_lon = 25.809554
    radius = 7.5


site_mappers.register(MetsimotlhabePlotMapper)


class MmadinarePlotMapper(Mapper):

    map_area = 'mmadinare'
    map_code = '26'
    intervention = False
    landmarks = None
    center_lat = -21.869753
    center_lon = 27.753179
    radius = 7.5


site_mappers.register(MmadinarePlotMapper)


class MmandunyanePlotMapper(Mapper):

    map_area = 'mmandunyane'
    map_code = '32'
    pair = 11
    intervention = False
    landmarks = None
    center_lat = -20.994015
    center_lon = 27.334564
    radius = 6.5


site_mappers.register(MmandunyanePlotMapper)


class MmankgodiPlotMapper(Mapper):

    map_area = 'mmankgodi'
    map_code = '19'
    pair = 5
    intervention = True
    landmarks = None
    center_lat = -24.729837
    center_lon = 25.646853
    radius = 5.5


site_mappers.register(MmankgodiPlotMapper)


class MmathethePlotMapper(Mapper):

    map_area = 'mmathethe'
    map_code = '20'
    pair = 5
    intervention = False
    landmarks = None
    center_lat = -25.318327
    center_lon = 25.269320
    radius = 5.5


site_mappers.register(MmathethePlotMapper)


class MolapowabojangPlotMapper(Mapper):

    map_area = 'molapowabojang'
    map_code = '13'
    pair = 2
    intervention = False
    landmarks = None
    center_lat = -25.204009
    center_lon = 25.562754
    radius = 5.5


site_mappers.register(MolapowabojangPlotMapper)


class NataPlotMapper(Mapper):

    map_area = 'nata'
    map_code = '38'
    pair = 15
    intervention = False
    landmarks = None
    center_lat = -20.207917
    center_lon = 26.184711
    radius = 5.5


site_mappers.register(NataPlotMapper)


class NkangePlotMapper(Mapper):

    map_area = 'nkange'
    map_code = '27'
    pair = 10
    intervention = True
    landmarks = None
    center_lat = -20.29269441
    center_lon = 27.13549895
    radius = 6.5


site_mappers.register(NkangePlotMapper)


class OodiPlotMapper(Mapper):

    map_area = 'oodi'
    map_code = '18'
    pair = 4
    intervention = True
    landmarks = None
    center_lat = -24.566840
    center_lon = 26.039595
    radius = 5.5


site_mappers.register(OodiPlotMapper)


class OtsePlotMapper(Mapper):

    map_area = 'otse'
    map_code = '14'
    pair = 2
    intervention = True
    landmarks = None
    center_lat = -25.033194
    center_lon = 25.747132
    radius = 5.5


site_mappers.register(OtsePlotMapper)


class RakopsPlotMapper(Mapper):

    map_area = 'rakops'
    map_code = '33'
    pair = 12
    intervention = False
    landmarks = None
    center_lat = -21.034979
    center_lon = 24.401214
    radius = 5.5


site_mappers.register(RakopsPlotMapper)


class RamokgonamiPlotMapper(Mapper):

    map_area = 'ramokgonami'
    map_code = '24'
    pair = 7
    intervention = False
    landmarks = None
    center_lat = -22.8658437618
    center_lon = 27.4198811366
    radius = 5.5


site_mappers.register(RamokgonamiPlotMapper)


class RanakaPlotMapper(Mapper):

    map_area = 'ranaka'
    map_code = '11'
    pair = 1
    intervention = False
    landmarks = None
    center_lat = -24.908703
    center_lon = 25.463033
    radius = 4


site_mappers.register(RanakaPlotMapper)


class SebinaPlotMapper(Mapper):

    map_area = 'sebina'
    map_code = '28'
    pair = 10
    intervention = False
    landmarks = None
    center_lat = -20.806103
    center_lon = 27.200003
    radius = 6.5


site_mappers.register(SebinaPlotMapper)


class SefharePlotMapper(Mapper):

    map_area = 'sefhare'
    map_code = '39'
    pair = 14
    intervention = True
    landmarks = None
    center_lat = -23.027271
    center_lon = 27.526095
    radius = 5.5


site_mappers.register(SefharePlotMapper)


class SefophePlotMapper(Mapper):

    map_area = 'sefophe'
    map_code = '22'
    pair = 6
    intervention = False
    landmarks = None
    center_lat = -22.1918153
    center_lon = 27.9624366
    radius = 5.5


site_mappers.register(SefophePlotMapper)


class ShakawePlotMapper(Mapper):

    map_area = 'shakawe'
    map_code = '36'
    pair = 13
    intervention = False
    landmarks = None
    center_lat = -18.360902
    center_lon = 21.836862
    radius = 11


site_mappers.register(ShakawePlotMapper)


class ShoshongPlotMapper(Mapper):

    map_area = 'shoshong'
    map_code = '25'
    pair = 8
    intervention = True
    landmarks = None
    center_lat = -23.032546
    center_lon = 26.516352
    radius = 6.0


site_mappers.register(ShoshongPlotMapper)


class TatiSidingPlotMapper(Mapper):

    map_area = 'tati_siding'
    map_code = '30'
    pair = 9
    intervention = True
    landmarks = None
    center_lat = -21.274018
    center_lon = 27.474822
    radius = 6.5


site_mappers.register(TatiSidingPlotMapper)


class TsetsebjwePlotMapper(Mapper):

    map_area = 'tsetsebjwe'
    map_code = '40'
    pair = 14
    intervention = False
    landmarks = None
    center_lat = -22.41391
    center_lon = 28.39465
    radius = 5.5


site_mappers.register(TsetsebjwePlotMapper)