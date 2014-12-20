from app import db

# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Index, Integer, LargeBinary, Numeric, SmallInteger, String, Table, Text, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class Accessgroup(db.Model):
    __tablename__ = 'accessgroup'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    group_id = Column(Integer)
    items = Column(Text)
    actions = Column(Integer)
    fomname = Column(String(60))
    nameitems = Column(Text)


class Akcia(db.Model):
    __tablename__ = 'akcia'

    kod = Column(Integer, primary_key=True)
    name = Column(String(255))
    datebegin = Column(Date)
    dateend = Column(Date)
    tipskidka = Column(SmallInteger)
    idtablskidka = Column(Integer)
    areal = Column(SmallInteger)
    statuscard = Column(Integer)


class Akcianame(db.Model):
    __tablename__ = 'akcianame'

    kod = Column(Integer, primary_key=True)
    idakcia = Column(ForeignKey('akcia.kod'))
    idname = Column(ForeignKey('name.kod'))
    cenapoakcia = Column(Numeric(15, 2))

    akcia = relationship('Akcia')
    name = relationship('Name')


t_amv = Table(
    'amv', metadata,
    Column('nomkod', Integer),
    Column('krossnomer', Integer),
    Column('kodsklada', SmallInteger),
    Column('kodmat', String(15)),
    Column('datadoc', Date),
    Column('tipdoc', SmallInteger),
    Column('kodpartnera', Integer),
    Column('nomer', String(15)),
    Column('cenaprix', Numeric(15, 2)),
    Column('cenarasx', Numeric(15, 2)),
    Column('cenazav', Numeric(15, 5)),
    Column('cenaval', Numeric(15, 5)),
    Column('cenatam', Numeric(15, 5)),
    Column('cenaunskidka', Numeric(15, 2)),
    Column('kolvo', Numeric(15, 3)),
    Column('perebros', String(1)),
    Column('bodydoc', Integer),
    Column('kolvodoc', Numeric(15, 3)),
    Column('cenarozn', Numeric(15, 2)),
    Column('kolret', Float),
    Column('kolbreak', Float),
    Column('grupschet', String(1)),
    Column('namekod', Integer),
    Column('kodkassa', Integer),
    Column('skidka', Numeric(6, 2)),
    Column('kolvodrob', Integer),
    Column('cenadrob', Numeric(15, 2)),
    Column('cenadrobunskd', Numeric(15, 2)),
    Column('cenarbeznds', Numeric(15, 2)),
    Index('amv_idx1', 'kodsklada', 'kodmat'),
    Index('amv_idx3', 'kodmat', 'tipdoc')
)


class Apttovar(db.Model):
    __tablename__ = 'apttovar'
    __table_args__ = (
        Index('apttovar_idx1', 'kodapt', 'kodname', 'datekolvo'),
    )

    id = Column(Integer, primary_key=True)
    kodapt = Column(Integer)
    kodname = Column(Integer)
    kolvo = Column(Float)
    datekolvo = Column(Date)
    pr_kolvo = Column(Float)
    pr_sump = Column(Float)
    pr_sumr = Column(Float)
    rs_kolvo = Column(Float)
    rs_sump = Column(Float)
    rs_sumr = Column(Float)
    rs_sumdoc = Column(Float)
    prihod = Column(Float)
    rozn = Column(Float)


t_arhivcen = Table(
    'arhivcen', metadata,
    Column('kod', String(15), unique=True),
    Column('name', String(80)),
    Column('priceprixod', Numeric(15, 5)),
    Column('pricereal1', Numeric(15, 2)),
    Column('pricereal2', Numeric(15, 2)),
    Column('pricereal3', Numeric(15, 2)),
    Column('izmerenie', String(3)),
    Column('upakovka', String(10)),
    Column('minzapas', SmallInteger),
    Column('incnds', String(1)),
    Column('procincnds', Float),
    Column('dbefor', Date),
    Column('klasskod', Integer),
    Column('groupkod', Integer),
    Column('namekod', Integer),
    Column('dateinbase', Date),
    Column('seria', String(30)),
    Column('pricetam', Numeric(15, 5)),
    Column('takecommon', String(1)),
    Column('lastdatepr', Date),
    Column('lastdaters', Date),
    Column('kodfpost', Integer),
    Column('zapret', String(1)),
    Column('tovarsh', String(1)),
    Column('kodkassa', Integer),
    Column('pricevaluta', Float),
    Column('privazka', String(1)),
    Column('pricezavod', Float),
    Column('tipvalut', String(10)),
    Column('pricereal4', Numeric(15, 2)),
    Column('pricereal5', Numeric(15, 2)),
    Column('pricereal6', Numeric(15, 2)),
    Column('nosale', String(1)),
    Column('nosaledate', Date),
    Column('kodcertf', Integer),
    Column('grup', Integer),
    Column('nomsertf', String(15)),
    Column('datesertf', Date),
    Column('nommonthuc', SmallInteger),
    Column('ucenkayes', String(1)),
    Column('nomerprot', String(15)),
    Column('dateprot', Date),
    Column('kodparent', String(15)),
    Column('strihcod', String(13)),
    Column('cpostnomer', String(15)),
    Column('cpostdate', Date),
    Column('cnomer', String(15))
)


class Assortiment(db.Model):
    __tablename__ = 'assortiment'

    kodapt = Column(Integer, primary_key=True, nullable=False)
    kodname = Column(Integer, primary_key=True, nullable=False)
    minzapas = Column(Numeric(15, 3))
    maxzapas = Column(Numeric(15, 3))
    typeact = Column(SmallInteger)
    abc = Column(SmallInteger)
    lastupd = Column(Date)
    dateperiod = Column(Date)


t_badm = Table(
    'badm', metadata,
    Column('kl', String(20)),
    Column('kfp', String(20)),
    Column('kn', Integer)
)


t_bank = Table(
    'bank', metadata,
    Column('mfo', Integer, unique=True),
    Column('name', String(35)),
    Column('city', String(25))
)


t_boln = Table(
    'boln', metadata,
    Column('kod', Integer, nullable=False),
    Column('name', String(100)),
    Column('adres', String(100)),
    Column('seria', Text(5)),
    Column('udost', String(10)),
    Column('kateg', SmallInteger),
    Column('ambul', String(10)),
    Column('recept', String(10)),
    Column('speckod', Text(1)),
    Column('insulin', String(40))
)


t_cenkod = Table(
    'cenkod', metadata,
    Column('kod', Integer)
)

# FixMe: was:
# class Cennik(Base):
class Cennik(db.Model):
    __tablename__ = 'cennik'

    kod = Column(String(15), primary_key=True)
    name = Column(String(80))
    priceprixod = Column(Numeric(15, 5))
    pricereal1 = Column(Numeric(15, 2))
    pricereal2 = Column(Numeric(15, 2))
    pricereal3 = Column(Numeric(15, 2))
    izmerenie = Column(String(3))
    upakovka = Column(String(10))
    minzapas = Column(SmallInteger)
    incnds = Column(String(1))
    procincnds = Column(Float)
    dbefor = Column(Date)
    klasskod = Column(ForeignKey('klass.kod'))
    groupkod = Column(ForeignKey('grup.kod'))
    namekod = Column(ForeignKey('name.kod'))
    dateinbase = Column(Date)
    seria = Column(String(30))
    pricetam = Column(Numeric(15, 5))
    takecommon = Column(String(1))
    lastdatepr = Column(Date)
    lastdaters = Column(Date)
    kodfpost = Column(ForeignKey('postavka.kod'))
    zapret = Column(String(1))
    tovarsh = Column(String(1))
    kodkassa = Column(Integer)
    pricevaluta = Column(Numeric(15, 5))
    privazka = Column(String(1))
    pricezavod = Column(Numeric(15, 5))
    tipvalut = Column(String(10))
    pricereal4 = Column(Numeric(15, 2))
    pricereal5 = Column(Numeric(15, 2))
    pricereal6 = Column(Numeric(15, 2))
    nosale = Column(String(1))
    nosaledate = Column(Date)
    kodcertf = Column(Integer)
    grup = Column(Integer)
    nomsertf = Column(String(15))
    datesertf = Column(Date)
    nommonthuc = Column(SmallInteger)
    ucenkayes = Column(String(1))
    nomerprot = Column(String(15))
    dateprot = Column(Date)
    kodparent = Column(String(15))
    strihcod = Column(String(13))
    cpostnomer = Column(String(15))
    cpostdate = Column(Date)
    cnomer = Column(String(15))

    grup1 = relationship('Grup')
    klas = relationship('Klas')
    postavka = relationship('Postavka')
    name1 = relationship('Name')


t_cennik_log = Table(
    'cennik_log', metadata,
    Column('kod', String(15)),
    Column('name', String(80)),
    Column('priceprixod', Numeric(15, 5)),
    Column('pricereal1', Numeric(15, 2)),
    Column('pricereal2', Numeric(15, 2)),
    Column('pricereal3', Numeric(15, 2)),
    Column('izmerenie', String(3)),
    Column('upakovka', String(10)),
    Column('minzapas', SmallInteger),
    Column('incnds', String(1)),
    Column('procincnds', Float),
    Column('dbefor', Date),
    Column('klasskod', Integer),
    Column('groupkod', Integer),
    Column('namekod', Integer),
    Column('dateinbase', Date),
    Column('seria', String(30)),
    Column('pricetam', Numeric(15, 5)),
    Column('takecommon', String(1)),
    Column('lastdatepr', Date),
    Column('lastdaters', Date),
    Column('kodfpost', Integer),
    Column('zapret', String(1)),
    Column('tovarsh', String(1)),
    Column('kodkassa', Integer),
    Column('pricevaluta', Numeric(15, 5)),
    Column('privazka', String(1)),
    Column('pricezavod', Numeric(15, 5)),
    Column('tipvalut', String(10)),
    Column('pricereal4', Numeric(15, 2)),
    Column('pricereal5', Numeric(15, 2)),
    Column('pricereal6', Numeric(15, 2)),
    Column('nosale', String(1)),
    Column('nosaledate', Date),
    Column('kodcertf', Integer),
    Column('grup', Integer),
    Column('nomsertf', String(15)),
    Column('datesertf', Date),
    Column('nommonthuc', SmallInteger),
    Column('ucenkayes', String(1)),
    Column('nomerprot', String(15)),
    Column('dateprot', Date),
    Column('kodparent', String(15)),
    Column('strihcod', String(13)),
    Column('cpostnomer', String(15)),
    Column('cpostdate', Date),
    Column('cnomer', String(15)),
    Column('dateoper', DateTime),
    Column('tipoper', Text(1))
)


class Collector(db.Model):
    __tablename__ = 'collector'

    kod = Column(Integer, primary_key=True)
    name = Column(String(40))


t_com_mv = Table(
    'com_mv', metadata,
    Column('nomkod', Numeric(scale=0)),
    Column('krossnomer', Numeric(scale=0)),
    Column('kodsklada', Numeric(scale=0)),
    Column('kodmat', String(15)),
    Column('datadoc', Date),
    Column('tipdoc', Numeric(scale=0)),
    Column('kodpartnera', Numeric(scale=0)),
    Column('nomer', String(15)),
    Column('cenaprix', Float),
    Column('cenarasx', Float),
    Column('cenazav', Float),
    Column('cenaval', Float),
    Column('cenatam', Float),
    Column('cenaunskidka', Float),
    Column('kolvo', Float),
    Column('perebros', String(1)),
    Column('bodydoc', Numeric(scale=0)),
    Column('kolvodoc', Float),
    Column('cenarozn', Float),
    Column('kolret', Float),
    Column('kolbreak', Float),
    Column('grupschet', String(1)),
    Column('namekod', Numeric(scale=0)),
    Column('kodkassa', Numeric(scale=0)),
    Column('skidka', Numeric(scale=2))
)


t_comperecen = Table(
    'comperecen', metadata,
    Column('nomer', Integer),
    Column('datep', Date),
    Column('sumskl', Float),
    Column('sumcen1', Float),
    Column('sumcen2', Float),
    Column('sumcen3', Float),
    Column('sumcen4', Float),
    Column('sumcen5', Float),
    Column('sumcen6', Float),
    Column('tip', SmallInteger)
)


t_corectdoza = Table(
    'corectdoza', metadata,
    Column('kodname', Integer),
    Column('cd_1', Float),
    Column('cd_2', Float),
    Column('cd_3', Float),
    Column('cd_4', Float),
    Column('cd_5', Float),
    Column('cd_6', Float),
    Column('cd_7', Float),
    Column('cd_8', Float),
    Column('cd_9', Float),
    Column('cd_10', Float),
    Column('cd_11', Float)
)


t_currency = Table(
    'currency', metadata,
    Column('id', Integer),
    Column('datecurrency', Date),
    Column('tipcur', SmallInteger),
    Column('cursale', Float),
    Column('curnbu', Float)
)


t_czak = Table(
    'czak', metadata,
    Column('nomkod', Numeric(scale=0)),
    Column('krossnomer', Numeric(scale=0)),
    Column('kodsklada', Numeric(scale=0)),
    Column('kodmat', String(15)),
    Column('datadoc', Date),
    Column('tipdoc', Numeric(scale=0)),
    Column('kodpartnera', Numeric(scale=0)),
    Column('nomer', String(15)),
    Column('cenaprix', Float),
    Column('cenarasx', Float),
    Column('cenazav', Float),
    Column('cenaval', Float),
    Column('cenatam', Float),
    Column('cenaunskidka', Float),
    Column('kolvo', Float),
    Column('perebros', String(1)),
    Column('bodydoc', Numeric(scale=0)),
    Column('kolvodoc', Float),
    Column('cenarozn', Float),
    Column('kolret', Float),
    Column('kolbreak', Float),
    Column('grupschet', String(1)),
    Column('kod', String(15)),
    Column('namekod', Numeric(scale=0)),
    Column('kodnm', Numeric(scale=0)),
    Column('nametext', String(80)),
    Column('tipimport', String(1))
)


t_czak1 = Table(
    'czak1', metadata,
    Column('nomkod', Numeric(scale=0)),
    Column('krossnomer', Numeric(scale=0)),
    Column('kodsklada', Numeric(scale=0)),
    Column('kodmat', String(15)),
    Column('datadoc', Date),
    Column('tipdoc', Numeric(scale=0)),
    Column('kodpartnera', Numeric(scale=0)),
    Column('nomer', String(15)),
    Column('cenaprix', Float),
    Column('cenarasx', Float),
    Column('cenazav', Float),
    Column('cenaval', Float),
    Column('cenatam', Float),
    Column('cenaunskidka', Float),
    Column('kolvo', Float),
    Column('perebros', String(1)),
    Column('bodydoc', Numeric(scale=0)),
    Column('kolvodoc', Float),
    Column('cenarozn', Float),
    Column('kolret', Float),
    Column('kolbreak', Float),
    Column('grupschet', String(1)),
    Column('kod', String(15)),
    Column('namekod', Numeric(scale=0)),
    Column('kodnm', Numeric(scale=0)),
    Column('nametext', String(80)),
    Column('tipimport', String(1))
)


t_czak2 = Table(
    'czak2', metadata,
    Column('nomkod', Numeric(scale=0)),
    Column('krossnomer', Numeric(scale=0)),
    Column('kodsklada', Numeric(scale=0)),
    Column('kodmat', String(15)),
    Column('datadoc', Date),
    Column('tipdoc', Numeric(scale=0)),
    Column('kodpartnera', Numeric(scale=0)),
    Column('nomer', String(15)),
    Column('cenaprix', Float),
    Column('cenarasx', Float),
    Column('cenazav', Float),
    Column('cenaval', Float),
    Column('cenatam', Float),
    Column('cenaunskidka', Float),
    Column('kolvo', Float),
    Column('perebros', String(1)),
    Column('bodydoc', Numeric(scale=0)),
    Column('kolvodoc', Float),
    Column('cenarozn', Float),
    Column('kolret', Float),
    Column('kolbreak', Float),
    Column('grupschet', String(1))
)


class Disclogimport(db.Model):
    __tablename__ = 'disclogimport'

    kod = Column(Integer, primary_key=True)
    kodapt = Column(Integer)
    krossdoc = Column(Integer)
    summa = Column(Float)
    dcard = Column(Integer)


class Discount(db.Model):
    __tablename__ = 'discount'

    kod = Column(Integer, primary_key=True)
    name = Column(String(30))
    otch = Column(String(30))
    fam = Column(String(50))
    dateborn = Column(Date)
    city = Column(String(30))
    street = Column(String(50))
    house = Column(String(10))
    flat = Column(Text(3))
    phone = Column(String(50))
    email = Column(String(70))
    summa = Column(Float)
    datecr = Column(Date)
    cardkod = Column(String(13))
    i1 = Column(SmallInteger)
    i2 = Column(SmallInteger)
    i3 = Column(SmallInteger)
    i4 = Column(SmallInteger)
    i5 = Column(SmallInteger)
    i6 = Column(SmallInteger)
    i7 = Column(SmallInteger)
    i8 = Column(SmallInteger)
    i9 = Column(SmallInteger)
    i10 = Column(SmallInteger)
    m1 = Column(SmallInteger)
    m2 = Column(SmallInteger)
    m3 = Column(SmallInteger)
    m4 = Column(SmallInteger)
    m5 = Column(SmallInteger)
    m6 = Column(SmallInteger)
    m7 = Column(SmallInteger)
    dr_i = Column(String(50))
    dr_m = Column(String(50))
    dr_s = Column(String(40))
    status = Column(String(15))
    vydal = Column(String(40))
    raion = Column(String(30))
    oblast = Column(String(30))
    postind = Column(Text(6))
    blockcard = Column(SmallInteger)


t_doc_1 = Table(
    'doc_1', metadata,
    Column('nomer', Integer),
    Column('kod_mat', String(15)),
    Column('kod_klass', Integer),
    Column('kod_group', Integer),
    Column('kod_name', Integer),
    Column('name_mat', String(40)),
    Column('cena_pr', Float),
    Column('cena_ot', Float),
    Column('summa', Float),
    Column('kolvo', Float),
    Column('ed_iz', String(3)),
    Column('seria', String(10)),
    Column('tamprice', Float),
    Column('dat_real', Date),
    Column('priceunskidka', Float),
    Column('valuta', Float),
    Column('c_kodreplace', String(255)),
    Column('tiperror', String(3)),
    Column('kodmstate', Integer),
    Column('krossn', Integer),
    Column('handnom', String(15)),
    Column('tipd', SmallInteger),
    Column('kodskl', SmallInteger),
    Column('ddoc', Date),
    Column('tpereb', String(1)),
    Column('kodpart', Integer),
    Column('tnds', String(1)),
    Column('cenafromcen', Float)
)


t_doc_10 = Table(
    'doc_10', metadata,
    Column('nomer', Integer),
    Column('kod_mat', String(15)),
    Column('kod_klass', Integer),
    Column('kod_group', Integer),
    Column('kod_name', Integer),
    Column('name_mat', String(40)),
    Column('cena_pr', Float),
    Column('cena_ot', Float),
    Column('summa', Float),
    Column('kolvo', Float),
    Column('ed_iz', String(3)),
    Column('seria', String(10)),
    Column('tamprice', Float),
    Column('dat_real', Date),
    Column('priceunskidka', Float),
    Column('valuta', Float),
    Column('c_kodreplace', String(255)),
    Column('tiperror', String(3)),
    Column('kodmstate', Integer),
    Column('krossn', Integer),
    Column('handnom', String(15)),
    Column('tipd', SmallInteger),
    Column('kodskl', SmallInteger),
    Column('ddoc', Date),
    Column('tpereb', String(1)),
    Column('kodpart', Integer),
    Column('tnds', String(1)),
    Column('cenafromcen', Float)
)


t_doc_100 = Table(
    'doc_100', metadata,
    Column('nomer', Integer),
    Column('kod_mat', String(15)),
    Column('kod_klass', Integer),
    Column('kod_group', Integer),
    Column('kod_name', Integer),
    Column('name_mat', String(40)),
    Column('cena_pr', Float),
    Column('cena_ot', Float),
    Column('summa', Float),
    Column('kolvo', Float),
    Column('ed_iz', String(3)),
    Column('seria', String(10)),
    Column('tamprice', Float),
    Column('dat_real', Date),
    Column('priceunskidka', Float),
    Column('valuta', Float),
    Column('c_kodreplace', String(255)),
    Column('tiperror', String(3)),
    Column('kodmstate', Integer),
    Column('krossn', Integer),
    Column('handnom', String(15)),
    Column('tipd', SmallInteger),
    Column('kodskl', SmallInteger),
    Column('ddoc', Date),
    Column('tpereb', String(1)),
    Column('kodpart', Integer),
    Column('tnds', String(1)),
    Column('cenafromcen', Float)
)


t_doc_1001 = Table(
    'doc_1001', metadata,
    Column('nomer', Integer),
    Column('kod_mat', String(15)),
    Column('kod_klass', Integer),
    Column('kod_group', Integer),
    Column('kod_name', Integer),
    Column('name_mat', String(40)),
    Column('cena_pr', Float),
    Column('cena_ot', Float),
    Column('summa', Float),
    Column('kolvo', Float),
    Column('ed_iz', String(3)),
    Column('seria', String(10)),
    Column('tamprice', Float),
    Column('dat_real', Date),
    Column('priceunskidka', Float),
    Column('valuta', Float),
    Column('c_kodreplace', String(255)),
    Column('tiperror', String(3)),
    Column('kodmstate', Integer),
    Column('krossn', Integer),
    Column('handnom', String(15)),
    Column('tipd', SmallInteger),
    Column('kodskl', SmallInteger),
    Column('ddoc', Date),
    Column('tpereb', String(1)),
    Column('kodpart', Integer),
    Column('tnds', String(1)),
    Column('cenafromcen', Float)
)


t_doc_2 = Table(
    'doc_2', metadata,
    Column('nomer', Integer),
    Column('kod_mat', String(15)),
    Column('kod_klass', Integer),
    Column('kod_group', Integer),
    Column('kod_name', Integer),
    Column('name_mat', String(40)),
    Column('cena_pr', Float),
    Column('cena_ot', Float),
    Column('summa', Float),
    Column('kolvo', Float),
    Column('ed_iz', String(3)),
    Column('seria', String(10)),
    Column('tamprice', Float),
    Column('dat_real', Date),
    Column('priceunskidka', Float),
    Column('valuta', Float),
    Column('c_kodreplace', String(255)),
    Column('tiperror', String(3)),
    Column('kodmstate', Integer),
    Column('krossn', Integer),
    Column('handnom', String(15)),
    Column('tipd', SmallInteger),
    Column('kodskl', SmallInteger),
    Column('ddoc', Date),
    Column('tpereb', String(1)),
    Column('kodpart', Integer),
    Column('tnds', String(1)),
    Column('cenafromcen', Float)
)


t_doc_20 = Table(
    'doc_20', metadata,
    Column('nomer', Integer),
    Column('kod_mat', String(15)),
    Column('kod_klass', Integer),
    Column('kod_group', Integer),
    Column('kod_name', Integer),
    Column('name_mat', String(40)),
    Column('cena_pr', Float),
    Column('cena_ot', Float),
    Column('summa', Float),
    Column('kolvo', Float),
    Column('ed_iz', String(3)),
    Column('seria', String(10)),
    Column('tamprice', Float),
    Column('dat_real', Date),
    Column('priceunskidka', Float),
    Column('valuta', Float),
    Column('c_kodreplace', String(255)),
    Column('tiperror', String(3)),
    Column('kodmstate', Integer),
    Column('krossn', Integer),
    Column('handnom', String(15)),
    Column('tipd', SmallInteger),
    Column('kodskl', SmallInteger),
    Column('ddoc', Date),
    Column('tpereb', String(1)),
    Column('kodpart', Integer),
    Column('tnds', String(1)),
    Column('cenafromcen', Float)
)


t_doc_21 = Table(
    'doc_21', metadata,
    Column('nomer', Integer),
    Column('kod_mat', String(15)),
    Column('kod_klass', Integer),
    Column('kod_group', Integer),
    Column('kod_name', Integer),
    Column('name_mat', String(40)),
    Column('cena_pr', Float),
    Column('cena_ot', Float),
    Column('summa', Float),
    Column('kolvo', Float),
    Column('ed_iz', String(3)),
    Column('seria', String(10)),
    Column('tamprice', Float),
    Column('dat_real', Date),
    Column('priceunskidka', Float),
    Column('valuta', Float),
    Column('c_kodreplace', String(255)),
    Column('tiperror', String(3)),
    Column('kodmstate', Integer),
    Column('krossn', Integer),
    Column('handnom', String(15)),
    Column('tipd', SmallInteger),
    Column('kodskl', SmallInteger),
    Column('ddoc', Date),
    Column('tpereb', String(1)),
    Column('kodpart', Integer),
    Column('tnds', String(1)),
    Column('cenafromcen', Float)
)


t_doc_3 = Table(
    'doc_3', metadata,
    Column('nomer', Integer),
    Column('kod_mat', String(15)),
    Column('kod_klass', Integer),
    Column('kod_group', Integer),
    Column('kod_name', Integer),
    Column('name_mat', String(40)),
    Column('cena_pr', Float),
    Column('cena_ot', Float),
    Column('summa', Float),
    Column('kolvo', Float),
    Column('ed_iz', String(3)),
    Column('seria', String(10)),
    Column('tamprice', Float),
    Column('dat_real', Date),
    Column('priceunskidka', Float),
    Column('valuta', Float),
    Column('c_kodreplace', String(255)),
    Column('tiperror', String(3)),
    Column('kodmstate', Integer),
    Column('krossn', Integer),
    Column('handnom', String(15)),
    Column('tipd', SmallInteger),
    Column('kodskl', SmallInteger),
    Column('ddoc', Date),
    Column('tpereb', String(1)),
    Column('kodpart', Integer),
    Column('tnds', String(1)),
    Column('cenafromcen', Float)
)


t_doc_9 = Table(
    'doc_9', metadata,
    Column('nomer', Integer),
    Column('kod_mat', String(15)),
    Column('kod_klass', Integer),
    Column('kod_group', Integer),
    Column('kod_name', Integer),
    Column('name_mat', String(40)),
    Column('cena_pr', Float),
    Column('cena_ot', Float),
    Column('summa', Float),
    Column('kolvo', Float),
    Column('ed_iz', String(3)),
    Column('seria', String(10)),
    Column('tamprice', Float),
    Column('dat_real', Date),
    Column('priceunskidka', Float),
    Column('valuta', Float),
    Column('c_kodreplace', String(255)),
    Column('tiperror', String(3)),
    Column('kodmstate', Integer),
    Column('krossn', Integer),
    Column('handnom', String(15)),
    Column('tipd', SmallInteger),
    Column('kodskl', SmallInteger),
    Column('ddoc', Date),
    Column('tpereb', String(1)),
    Column('kodpart', Integer),
    Column('tnds', String(1)),
    Column('cenafromcen', Float)
)


t_doc_999 = Table(
    'doc_999', metadata,
    Column('nomer', Integer),
    Column('kod_mat', String(15)),
    Column('kod_klass', Integer),
    Column('kod_group', Integer),
    Column('kod_name', Integer),
    Column('name_mat', String(40)),
    Column('cena_pr', Float),
    Column('cena_ot', Float),
    Column('summa', Float),
    Column('kolvo', Float),
    Column('ed_iz', String(3)),
    Column('seria', String(10)),
    Column('tamprice', Float),
    Column('dat_real', Date),
    Column('priceunskidka', Float),
    Column('valuta', Float),
    Column('c_kodreplace', String(255)),
    Column('tiperror', String(3)),
    Column('kodmstate', Integer),
    Column('krossn', Integer),
    Column('handnom', String(15)),
    Column('tipd', SmallInteger),
    Column('kodskl', SmallInteger),
    Column('ddoc', Date),
    Column('tpereb', String(1)),
    Column('kodpart', Integer),
    Column('tnds', SmallInteger),
    Column('cenafromcen', Float)
)


t_doc_rasx = Table(
    'doc_rasx', metadata,
    Column('nomer', Integer),
    Column('kod_mat', String(15)),
    Column('kod_klass', Integer),
    Column('kod_group', Integer),
    Column('kod_name', Integer),
    Column('name_mat', String(80)),
    Column('cena_pr', Numeric(15, 5)),
    Column('cena_ot', Numeric(15, 2)),
    Column('summa', Float),
    Column('kolvo', Numeric(15, 3)),
    Column('ed_iz', String(3)),
    Column('seria', String(10)),
    Column('tamprice', Numeric(15, 5)),
    Column('dat_real', Date),
    Column('priceunskidka', Numeric(15, 2)),
    Column('valuta', Numeric(15, 5)),
    Column('c_kodreplace', String(255)),
    Column('tiperror', String(3)),
    Column('kodmstate', Integer),
    Column('krossn', Integer),
    Column('handnom', String(15)),
    Column('tipd', SmallInteger),
    Column('kodskl', SmallInteger),
    Column('ddoc', Date),
    Column('tpereb', String(1)),
    Column('kodpart', Integer),
    Column('tnds', SmallInteger),
    Column('cenafromcen', Numeric(15, 2)),
    Column('procval', Float),
    Column('cenarbeznds', Numeric(15, 2))
)


class Doctor(db.Model):
    __tablename__ = 'doctor'

    kod = Column(Integer, primary_key=True)
    name = Column(String(80))
    kodhosp = Column(Integer)


t_document = Table(
    'document', metadata,
    Column('nomer', Integer),
    Column('kod_mat', String(15)),
    Column('kod_klass', Integer),
    Column('kod_group', Integer),
    Column('kod_name', Integer),
    Column('name_mat', String(80)),
    Column('cena_pr', Float),
    Column('cena_ot', Numeric(15, 2)),
    Column('summa', Float),
    Column('kolvo', Numeric(15, 3)),
    Column('ed_iz', String(3)),
    Column('seria', String(30)),
    Column('tamprice', Float),
    Column('dat_real', Date),
    Column('koef', Float),
    Column('cena_roznica', Numeric(15, 2)),
    Column('kassa', Integer),
    Column('krossn', Integer),
    Column('handnom', String(15)),
    Column('tipd', SmallInteger),
    Column('kodskl', SmallInteger),
    Column('tpereb', String(1)),
    Column('kodpart', Integer),
    Column('ddoc', Date),
    Column('valprice', Float),
    Column('zavodprice', Float),
    Column('tipval', String(10)),
    Column('kodplace', String(155)),
    Column('priceunskidka', Float),
    Column('tiperror', String(1)),
    Column('kodmstate', Integer),
    Column('kodcertf', Integer),
    Column('certf', String(1)),
    Column('kolvoold', Numeric(15, 3)),
    Column('kolvodoc', Numeric(15, 3)),
    Column('nreg', String(15)),
    Column('datereg', Date),
    Column('nsertf', String(15)),
    Column('datesertf', Date),
    Column('upakovka', Integer),
    Column('naclist', SmallInteger)
)


t_dogovor = Table(
    'dogovor', metadata,
    Column('id', Integer, unique=True),
    Column('platel', Integer),
    Column('nomer', String(15)),
    Column('datedoc', Date),
    Column('dateplat', Date),
    Column('cutname', String(40)),
    Column('place', String(40)),
    Column('elplace', String(40)),
    Column('summa', Float),
    Column('summaopl', Float)
)


t_dopnameshkod = Table(
    'dopnameshkod', metadata,
    Column('kod', Integer, nullable=False),
    Column('namekod', Integer),
    Column('shkod', String(13))
)


t_doproz = Table(
    'doproz', metadata,
    Column('kod', Integer, index=True),
    Column('name', String(50)),
    Column('ambul', String(10)),
    Column('udost', String(10)),
    Column('recept', String(10)),
    Column('daterecept', Date),
    Column('kateg', SmallInteger),
    Column('kodhospital', Integer),
    Column('nomer', Integer),
    Column('doctor', String(50)),
    Column('seriau', String(5)),
    Column('idboln', Integer),
    Column('kinsulin', Integer)
)


class Dov(db.Model):
    __tablename__ = 'dov'

    kross = Column(Integer, primary_key=True)
    nomer = Column(Text(15))
    dated = Column(Date)
    fam = Column(String(30))


t_dover = Table(
    'dover', metadata,
    Column('kod', Integer, unique=True),
    Column('nomer', String(16)),
    Column('dated', Date),
    Column('fam', String(30)),
    Column('kodpart', Integer),
    Column('srokwork', Date),
    Column('tip', String(1))
)


class Edinica(db.Model):
    __tablename__ = 'edinica'

    kod = Column(Integer, primary_key=True)
    name = Column(String(4))


t_filial = Table(
    'filial', metadata,
    Column('kod', Integer, unique=True),
    Column('name', String(30)),
    Column('fio', String(30)),
    Column('email', String(40)),
    Column('okpo', Text(10)),
    Column('sumskl', Numeric(15, 2), server_default=text("0")),
    Column('sumroz', Numeric(15, 2), server_default=text("0")),
    Column('kodskla', Integer),
    Column('namefile', String(20)),
    Column('kodapt', Integer)
)


class Fixcena(db.Model):
    __tablename__ = 'fixcena'

    kod = Column(Integer, primary_key=True)
    namekod = Column(Integer)
    cena = Column(Float)
    nomerprikaza = Column(String(30))
    dataprikaza = Column(Date)


t_freekodart = Table(
    'freekodart', metadata,
    Column('datekod', Date)
)


t_freenalog = Table(
    'freenalog', metadata,
    Column('id', Integer),
    Column('datedoc', Date),
    Column('kodpartnera', Integer),
    Column('sumcom', Float),
    Column('sumnds', Float),
    Column('nametovar', String(40)),
    Column('nnds', String(15)),
    Column('vidnds', SmallInteger),
    Column('stavkands', Float)
)


t_globcen = Table(
    'globcen', metadata,
    Column('kod', String(15)),
    Column('name', String(80)),
    Column('priceprixod', Numeric(scale=5)),
    Column('pricereal1', Numeric(scale=2)),
    Column('pricereal2', Numeric(scale=2)),
    Column('pricereal3', Numeric(scale=2)),
    Column('izmerenie', String(3)),
    Column('upakovka', String(10)),
    Column('minzapas', Numeric(scale=0)),
    Column('incnds', String(1)),
    Column('procincnds', Float),
    Column('dbefor', Date),
    Column('klasskod', Numeric(scale=0)),
    Column('groupkod', Numeric(scale=0)),
    Column('namekod', Numeric(scale=0)),
    Column('dateinbase', Date),
    Column('seria', String(30)),
    Column('pricetam', Numeric(scale=5)),
    Column('takecommon', String(1)),
    Column('lastdatepr', Date),
    Column('lastdaters', Date),
    Column('kodfpost', Numeric(scale=0)),
    Column('zapret', String(1)),
    Column('tovarsh', String(1)),
    Column('kodkassa', Numeric(scale=0)),
    Column('pricevaluta', Float),
    Column('privazka', String(1)),
    Column('pricezavod', Float),
    Column('tipvalut', String(10)),
    Column('pricereal4', Numeric(scale=2)),
    Column('pricereal5', Numeric(scale=2)),
    Column('pricereal6', Numeric(scale=2)),
    Column('nosale', String(1)),
    Column('nosaledate', Date),
    Column('kodcertf', Numeric(scale=0)),
    Column('grup', Numeric(scale=0)),
    Column('nomsertf', String(15)),
    Column('datesertf', Date),
    Column('nommonthuc', Numeric(scale=0)),
    Column('ucenkayes', String(1)),
    Column('nomerprot', String(15)),
    Column('dateprot', Date),
    Column('kodparent', String(15)),
    Column('strihcod', String(13)),
    Column('cpostnomer', String(15)),
    Column('cpostdate', Date)
)


class Group(db.Model):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(100))


# FixMe: was:
# class Grup(Grup):
class Grup(db.Model):
    __tablename__ = 'grup'

    kod = Column(Integer, primary_key=True, unique=True)
    name = Column(String(30))
    shortname = Column(String(6))
    kod_in_klass = Column(Integer)
    kassakod = Column(Integer)


class Gurnal(db.Model):
    __tablename__ = 'gurnal'

    id = Column(Integer, primary_key=True)
    kodskl = Column(Integer)
    dateiz = Column(Date)
    cena_skl = Column(Float)
    cena_roz = Column(Float)
    kodtovara = Column(String(15))
    o_nalik = Column(Numeric(15, 3))
    n_nalik = Column(Numeric(15, 3))
    peresort = Column(SmallInteger)


t_holder = Table(
    'holder', metadata,
    Column('kod', Integer, nullable=False, unique=True),
    Column('name', String(40))
)


t_hospital = Table(
    'hospital', metadata,
    Column('kod', Integer, unique=True),
    Column('name', String(80))
)


# FixMe: was:
# class Ibe$report(db.Model):
class Ibereport(db.Model):
    __tablename__ = 'ibe$reports'

    ibe_report_id = Column('ibe$report_id', Integer, primary_key=True)
    ibe_report_parent_id = Column('ibe$report_parent_id', Integer, nullable=False)
    ibe_report_name = Column('ibe$report_name', String(100), nullable=False)
    ibe_report_source = Column('ibe$report_source', LargeBinary)
    ibe_report_rights = Column('ibe$report_rights', LargeBinary)
    ibe_report_is_report = Column('ibe$report_is_report', SmallInteger, nullable=False, server_default=text("0"))


t_importdoc = Table(
    'importdoc', metadata,
    Column('kod', Integer, nullable=False),
    Column('name', String(30)),
    Column('namesystable', String(20)),
    Column('rash', SmallInteger, server_default=text("1"))
)


t_inidata = Table(
    'inidata', metadata,
    Column('razdel', String(50)),
    Column('varlab', String(50)),
    Column('valflt', Float),
    Column('valstr', String(254)),
    Column('valint', Integer),
    Column('valbool', Text(1)),
    Column('valdatetime', Date)
)


class Inrastvor(db.Model):
    __tablename__ = 'inrastvor'

    kod = Column(Integer, primary_key=True)
    kodname = Column(Integer)
    kodras = Column(Integer)
    quntity = Column(Float)


class Intername(db.Model):
    __tablename__ = 'intername'

    kod = Column(Integer, primary_key=True)
    name = Column(String(30))
    kodpzak = Column(Integer)


t_kassa = Table(
    'kassa', metadata,
    Column('kod', Integer, nullable=False),
    Column('name', Text(30)),
    Column('summa', Numeric(15, 2)),
    Column('valuta', Text(4)),
    Column('closedoc', Integer)
)


class Kategoria(db.Model):
    __tablename__ = 'kategoria'

    kod = Column(Integer, primary_key=True)
    name = Column(String(50))


# FixMe: was
# class Klas(db.Model):
class Klas(db.Model):
    __tablename__ = 'klass'

    kod = Column(Integer, primary_key=True)
    name = Column(String(30))
    country = Column(String(20))
    skidka = Column(Float)
    holder = Column(Integer)


t_kodartikul = Table(
    'kodartikul', metadata,
    Column('kod', Integer),
    Column('name', String(40)),
    Column('kassa', SmallInteger)
)


t_kom_r_cat = Table(
    'kom_r_cat', metadata,
    Column('tipblok', Numeric(scale=0)),
    Column('kodmat', String(15)),
    Column('tipdoc', Numeric(scale=0)),
    Column('kolvo', Float),
    Column('cenaprix', Float),
    Column('datadoc', Date),
    Column('cenarasx', Float),
    Column('cenarozn', Float),
    Column('kodpartnera', Numeric(scale=0)),
    Column('nomer', String(15)),
    Column('krossnomer', Numeric(scale=0)),
    Column('kodplat', Numeric(scale=0)),
    Column('kod', Numeric(scale=0)),
    Column('name', String(40)),
    Column('kodsklada', Numeric(scale=0)),
    Column('namecat', String(50)),
    Column('kodcat', Numeric(scale=0)),
    Column('skidka', Float),
    Column('namekod', Numeric(scale=0))
)


t_kom_reestr = Table(
    'kom_reestr', metadata,
    Column('kodmat', String(15)),
    Column('tipdoc', Numeric(scale=0)),
    Column('kolvo', Float),
    Column('cenaprix', Numeric(scale=5)),
    Column('datadoc', Date),
    Column('cenarasx', Numeric(scale=2)),
    Column('cenarozn', Numeric(scale=2)),
    Column('kodpartnera', Numeric(scale=0)),
    Column('nomer', String(15)),
    Column('krossnomer', Numeric(scale=0)),
    Column('kodplat', Numeric(scale=0)),
    Column('kod', Numeric(scale=0)),
    Column('name', String(40)),
    Column('kodsklada', Numeric(scale=0)),
    Column('namekod', Numeric(scale=0)),
    Column('vidnds', Numeric(scale=0)),
    Column('stavkands', Float)
)


t_kom_reestr_arh = Table(
    'kom_reestr_arh', metadata,
    Column('kodmat', String(15)),
    Column('tipdoc', Numeric(scale=0)),
    Column('kolvo', Float),
    Column('cenaprix', Float),
    Column('datadoc', Date),
    Column('cenarasx', Float),
    Column('cenarozn', Float),
    Column('kodpartnera', Numeric(scale=0)),
    Column('nomer', String(15)),
    Column('krossnomer', Numeric(scale=0)),
    Column('kodplat', Numeric(scale=0)),
    Column('kod', Numeric(scale=0)),
    Column('name', String(40)),
    Column('kodsklada', Numeric(scale=0)),
    Column('namekod', Numeric(scale=0)),
    Column('vidnds', Numeric(scale=0)),
    Column('stavkands', Float)
)


t_kom_reestr_t = Table(
    'kom_reestr_t', metadata,
    Column('kodmat', String(15)),
    Column('tipdoc', Numeric(scale=0)),
    Column('kolvo', Float),
    Column('cenaprix', Numeric(scale=5)),
    Column('datadoc', Date),
    Column('cenarasx', Numeric(scale=2)),
    Column('cenarozn', Numeric(scale=2)),
    Column('kodpartnera', Numeric(scale=0)),
    Column('nomer', String(15)),
    Column('krossnomer', Numeric(scale=0)),
    Column('kodplat', Numeric(scale=0)),
    Column('kod', Numeric(scale=0)),
    Column('name', String(40)),
    Column('kodsklada', Numeric(scale=0))
)


t_kor_com = Table(
    'kor_com', metadata,
    Column('krossnom', Numeric(scale=0)),
    Column('nomer', String(15)),
    Column('sumcom', Float),
    Column('datedoc', Date),
    Column('kodskl', Numeric(scale=0)),
    Column('tipdoc', Numeric(scale=0)),
    Column('kodpartnera', Numeric(scale=0)),
    Column('oplata', String(1)),
    Column('name', String(40)),
    Column('sumoplata', Float),
    Column('predoplata', Numeric(scale=0)),
    Column('dogovor', Numeric(scale=0)),
    Column('datesrok', DateTime),
    Column('sumnds', Float),
    Column('tipnds', Numeric(scale=0)),
    Column('tipplatega', Numeric(scale=0)),
    Column('krossschet', Numeric(scale=0)),
    Column('bodydoc', Numeric(scale=0)),
    Column('arhiv', String(1)),
    Column('dateopl', Date),
    Column('postnomer', String(15)),
    Column('postdate', Date),
    Column('buxtrans', Text(1)),
    Column('sumtorgnac', Float),
    Column('skidka', Float),
    Column('nnds', String(15)),
    Column('tarif', Float),
    Column('use_id', String(40)),
    Column('dcard', Numeric(scale=0))
)


t_liky_name = Table(
    'liky_name', metadata,
    Column('kl', Text(7)),
    Column('kn', Integer)
)


class Listinv(db.Model):
    __tablename__ = 'listinv'

    kod = Column(Integer, primary_key=True)
    dateinv = Column(Date)
    coment = Column(String(150))
    workplace = Column(SmallInteger)
    livei = Column(SmallInteger)
    datelive = Column(DateTime)
    otpusk = Column(Numeric(15, 3))


class Listnabor(db.Model):
    __tablename__ = 'listnabor'

    kod = Column(Integer, primary_key=True)
    dat = Column(Date)
    name = Column(Text(40))


class Listprice(db.Model):
    __tablename__ = 'listprice'

    id = Column(Integer, primary_key=True)
    idpartner = Column(Integer)
    introdate = Column(Date)
    filepath = Column(String(150))
    laststrok = Column(Integer)
    datefile = Column(Date)
    sizepfile = Column(Integer)
    activ = Column(SmallInteger)


t_listskl = Table(
    'listskl', metadata,
    Column('kod', Integer, unique=True),
    Column('name', String(30)),
    Column('parentlevel', SmallInteger, index=True),
    Column('main', SmallInteger),
    Column('nds', SmallInteger),
    Column('nabor', SmallInteger),
    Column('nabor2', SmallInteger),
    Column('nabor3', SmallInteger)
)


class Logcollect(db.Model):
    __tablename__ = 'logcollect'

    idmv = Column(Integer, primary_key=True)
    kolvomv = Column(Float)
    kolvocol = Column(Float)
    tiperror = Column(SmallInteger)


t_looktrebskl = Table(
    'looktrebskl', metadata,
    Column('okpo', String(10)),
    Column('kodmat', String(15)),
    Column('zakaz', Numeric(scale=2)),
    Column('inwork', Numeric(scale=0)),
    Column('cena', Float),
    Column('treb', Numeric(scale=0)),
    Column('spname', Numeric(scale=0)),
    Column('name', String(80))
)


class Lowp(db.Model):
    __tablename__ = 'lowp'

    id = Column(Integer, primary_key=True)
    idpost = Column(Integer)
    datatitle = Column(String(30))
    dataline = Column(String(30))
    datadop = Column(String(30))
    cell_1 = Column(SmallInteger)
    cell_2 = Column(SmallInteger)
    cell_3 = Column(SmallInteger)
    cell_4 = Column(SmallInteger)
    cell_5 = Column(SmallInteger)
    cell_6 = Column(SmallInteger)
    cell_7 = Column(SmallInteger)
    cell_8 = Column(SmallInteger)
    cell_9 = Column(SmallInteger)
    cell_10 = Column(SmallInteger)
    cell_11 = Column(SmallInteger)
    cell_12 = Column(SmallInteger)
    cell_13 = Column(SmallInteger)
    cell_14 = Column(SmallInteger)


t_maxcena = Table(
    'maxcena', metadata,
    Column('namekod', Numeric(scale=0)),
    Column('priceprixod', Float),
    Column('pricereal1', Float),
    Column('pricereal2', Float),
    Column('pricereal3', Float),
    Column('pricereal4', Float),
    Column('pricereal5', Float),
    Column('pricereal6', Float)
)


t_maxcenag = Table(
    'maxcenag', metadata,
    Column('namekod', Numeric(scale=0)),
    Column('priceprixod', Float),
    Column('pricereal1', Float),
    Column('pricereal2', Float),
    Column('pricereal3', Float),
    Column('pricereal4', Float),
    Column('pricereal5', Float),
    Column('pricereal6', Float)
)


t_maxcenaskl = Table(
    'maxcenaskl', metadata,
    Column('namekod', Numeric(scale=0)),
    Column('priceprixod', Float),
    Column('pricereal1', Float),
    Column('pricereal2', Float),
    Column('pricereal3', Float),
    Column('pricereal4', Float),
    Column('pricereal5', Float),
    Column('pricereal6', Float)
)


class MbLook(db.Model):
    __tablename__ = 'mb_look'

    id = Column(Integer, primary_key=True)
    use_id = Column(String(40))
    kod = Column(String(15))
    adminp = Column(Text(1))
    prava = Column(String(60))


t_med_name = Table(
    'med_name', metadata,
    Column('kl', Integer),
    Column('kn', Integer)
)


t_medmin = Table(
    'medmin', metadata,
    Column('cenaprix', Numeric(scale=5)),
    Column('kolvo', Numeric(scale=3)),
    Column('summa', Numeric(scale=8)),
    Column('kodnm', Numeric(scale=0)),
    Column('nametext', String(80)),
    Column('tipimport', String(1)),
    Column('nameklas', String(30)),
    Column('kodprz', Numeric(scale=0))
)


t_medminpost = Table(
    'medminpost', metadata,
    Column('cenaprix', Numeric(scale=5)),
    Column('kolvo', Numeric(scale=3)),
    Column('summa', Numeric(scale=8)),
    Column('kodnm', Numeric(scale=0)),
    Column('nametext', String(80)),
    Column('tipimport', String(1)),
    Column('nameklas', String(30)),
    Column('kodprz', Numeric(scale=0)),
    Column('kodpost', Integer),
    Column('namepost', String(40))
)


t_mincena = Table(
    'mincena', metadata,
    Column('namekod', Numeric(scale=0)),
    Column('priceprixod', Float),
    Column('pricereal1', Float),
    Column('pricereal2', Float),
    Column('pricereal3', Float),
    Column('pricereal4', Float),
    Column('pricereal5', Float),
    Column('pricereal6', Float)
)


t_mincenag = Table(
    'mincenag', metadata,
    Column('namekod', Numeric(scale=0)),
    Column('priceprixod', Float),
    Column('pricereal1', Float),
    Column('pricereal2', Float),
    Column('pricereal3', Float),
    Column('pricereal4', Float),
    Column('pricereal5', Float),
    Column('pricereal6', Float)
)


t_mincenaskl = Table(
    'mincenaskl', metadata,
    Column('namekod', Numeric(scale=0)),
    Column('priceprixod', Float),
    Column('pricereal1', Float),
    Column('pricereal2', Float),
    Column('pricereal3', Float),
    Column('pricereal4', Float),
    Column('pricereal5', Float),
    Column('pricereal6', Float)
)


class Mstate(db.Model):
    __tablename__ = 'mstate'

    kod = Column(Integer, primary_key=True)
    kodpzak = Column(Integer)
    name = Column(String(40))


class Mv(db.Model):
    __tablename__ = 'mv'
    __table_args__ = (
        Index('mv_idx4', 'kodsklada', 'kodmat'),
    )

    nomkod = Column(Integer, primary_key=True)
    krossnomer = Column(Integer, index=True)
    kodsklada = Column(SmallInteger)
    kodmat = Column(String(15), index=True)
    datadoc = Column(Date)
    tipdoc = Column(SmallInteger)
    kodpartnera = Column(Integer, index=True)
    nomer = Column(String(15))
    cenaprix = Column(Numeric(15, 5))
    cenarasx = Column(Numeric(15, 2))
    cenazav = Column(Numeric(15, 5))
    cenaval = Column(Numeric(15, 5))
    cenatam = Column(Numeric(15, 5))
    cenaunskidka = Column(Numeric(15, 2))
    kolvo = Column(Numeric(15, 3))
    perebros = Column(String(1))
    bodydoc = Column(Integer)
    kolvodoc = Column(Numeric(15, 3))
    cenarozn = Column(Numeric(15, 2))
    kolret = Column(Float)
    kolbreak = Column(Float)
    grupschet = Column(String(1))
    namekod = Column(Integer, index=True)
    kodkassa = Column(Integer)
    skidka = Column(Numeric(6, 2))
    kolvodrob = Column(Integer)
    cenadrob = Column(Numeric(15, 2))
    cenadrobunskd = Column(Numeric(15, 2))
    cenarbeznds = Column(Numeric(15, 2))


class Mvc(db.Model):
    __tablename__ = 'mvc'

    krossnom = Column(Integer, primary_key=True)
    kodskl = Column(Integer)
    datedoc = Column(Date)
    tipdoc = Column(SmallInteger)
    kodpartnera = Column(Integer, index=True)
    nomer = Column(String(15))
    sumcom = Column(Float)
    sumtorgnac = Column(Float)
    sumnac = Column(Float)
    sumnds = Column(Float)
    sumoplata = Column(Float)
    perebros = Column(String(1))
    tipplatega = Column(SmallInteger)
    datesrok = Column(DateTime)
    tipnds = Column(SmallInteger)
    ndsinnac = Column(Float)
    oplata = Column(String(1))
    dateopl = Column(Date)
    skidka = Column(Float)
    schetopl = Column(String(1))
    otlschet = Column(String(1))
    krossschet = Column(Integer)
    predoplata = Column(Integer)
    dogovor = Column(Integer)
    tarif = Column(Float)
    trudoem = Column(Float)
    kodmake = Column(String(15), index=True)
    kodplstore = Column(Integer)
    gikolvo = Column(Float)
    skgotov = Column(Integer)
    bodydoc = Column(Integer)
    kolret = Column(Float)
    kolbreak = Column(Float)
    grupschet = Column(String(1))
    arhiv = Column(String(1))
    buxtrans = Column(Text(1))
    postnomer = Column(String(15))
    postdate = Column(Date)
    veteran = Column(Text(1))
    outfil = Column(Integer)
    sumskl = Column(Float)
    nnds = Column(String(15))
    nomwork = Column(SmallInteger)
    nameschet = Column(SmallInteger)
    dcard = Column(Integer)
    yesprint = Column(SmallInteger)
    idsborka = Column(Integer)
    idcollector = Column(Integer)
    counterror = Column(Integer)
    countnolook = Column(Integer)
    transkassa = Column(SmallInteger)
    checkdopinfo = Column(String(100))
    proektdoc = Column(SmallInteger, server_default=text("0"))
    datedover = Column(Date)
    famdover = Column(String(80))
    versiadoc = Column(SmallInteger)
    tipsaledoc = Column(SmallInteger)
    ndsdate = Column(Date)
    vidnds = Column(SmallInteger)
    stavkands = Column(Numeric(5, 2))
    sposob = Column(SmallInteger)


t_mvc_res = Table(
    'mvc_res', metadata,
    Column('krossnom', Integer),
    Column('kodskl', Integer),
    Column('datedoc', Date),
    Column('tipdoc', SmallInteger),
    Column('kodpartnera', Integer),
    Column('nomer', String(15)),
    Column('sumcom', Float),
    Column('sumtorgnac', Float),
    Column('sumnac', Float),
    Column('sumnds', Float),
    Column('sumoplata', Float),
    Column('perebros', String(1)),
    Column('tipplatega', SmallInteger),
    Column('datesrok', Date),
    Column('tipnds', SmallInteger),
    Column('ndsinnac', Float),
    Column('oplata', String(1)),
    Column('dateopl', Date),
    Column('skidka', Integer),
    Column('schetopl', String(1)),
    Column('otlschet', String(1)),
    Column('krossschet', Integer),
    Column('predoplata', Integer),
    Column('dogovor', Integer),
    Column('tarif', Float),
    Column('trudoem', Float),
    Column('kodmake', String(15)),
    Column('kodplstore', Integer),
    Column('gikolvo', Float),
    Column('skgotov', Integer),
    Column('bodydoc', Integer),
    Column('kolret', Float),
    Column('kolbreak', Float),
    Column('grupschet', String(1)),
    Column('arhiv', String(1)),
    Column('buxtrans', Text(1)),
    Column('postnomer', String(15)),
    Column('postdate', Date),
    Column('veteran', Text(1)),
    Column('nnds', Integer),
    Column('outfil', Integer),
    Column('sumskl', Float)
)


t_na1log = Table(
    'na1log', metadata,
    Column('kodskl', Integer),
    Column('kodmat', String(15)),
    Column('onalik', Float),
    Column('nnalik', Float),
    Column('ohardreserv', Float),
    Column('nhardreserv', Float),
    Column('osumroz', Float),
    Column('nsumroz', Float),
    Column('iduser', Integer),
    Column('vrem', Date),
    Column('mesac', SmallInteger),
    Column('god', Integer)
)


t_nabor = Table(
    'nabor', metadata,
    Column('kodnabor', Integer),
    Column('kodmat', Text(15)),
    Column('kolvo', Float)
)


t_nac = Table(
    'nac', metadata,
    Column('kod', Integer, unique=True),
    Column('name', String(30)),
    Column('summa', Float),
    Column('ontovar', String(1)),
    Column('ndsout', String(1)),
    Column('sumnds', Float),
    Column('vid', SmallInteger)
)


t_nacenka = Table(
    'nacenka', metadata,
    Column('krosskod', Integer),
    Column('name', String(15)),
    Column('datadoc', Date),
    Column('tipdoc', SmallInteger),
    Column('kodpartnera', Integer),
    Column('nomer', String(30)),
    Column('summa', Float),
    Column('sumnds', Float),
    Column('proc', Float),
    Column('vid', Integer),
    Column('ndsout', Text(1)),
    Column('ontovar', Text(1)),
    Column('kod', Integer)
)


t_nalogreestr = Table(
    'nalogreestr', metadata,
    Column('datedoc', Date),
    Column('tipnds', Numeric(scale=0)),
    Column('sumcom', Float),
    Column('sumnds', Float),
    Column('name', String(40)),
    Column('nnds', String(15)),
    Column('tipdoc', Numeric(scale=0)),
    Column('nomind', String(12)),
    Column('kodskl', Numeric(scale=0)),
    Column('postdate', Date),
    Column('vidnds', Numeric(scale=0)),
    Column('stavkands', Float)
)


class Name(db.Model):
    __tablename__ = 'name'

    kod = Column(Integer, primary_key=True, unique=True)
    kodklass = Column(ForeignKey('klass.kod'))
    kodgroup = Column(ForeignKey('grup.kod'))
    koded = Column(Integer)
    name = Column(String(80), index=True)
    nprice1 = Column(Float)
    nprice2 = Column(Float)
    nprice3 = Column(Float)
    incdoc = Column(String(1))
    stopnacenka = Column(String(1))
    kodvida = Column(SmallInteger)
    kodbc = Column(Integer)
    narkotik = Column(String(1))
    tiptov = Column(Integer)
    tipimport = Column(String(1))
    minzapas = Column(Float)
    maxzapas = Column(Float)
    tovzapas1 = Column(Float)
    tovzapas2 = Column(Float)
    nreg = Column(String(15))
    srokregb = Column(Date)
    srokrege = Column(Date)
    kodmstate = Column(Integer)
    kodplacestore = Column(String(155))
    shtrihkod = Column(String(15))
    intername = Column(Integer)
    prikaz251 = Column(String(1))
    lastcena = Column(String(1))
    olgtovar = Column(String(1))
    koddoc = Column(Integer)
    netregistr = Column(SmallInteger)
    allstop = Column(SmallInteger)
    checkk = Column(Integer)
    onlyrecept = Column(SmallInteger)
    kodparent = Column(Integer)
    upakovka = Column(Integer)
    analiztorg = Column(SmallInteger)
    notinzav = Column(SmallInteger)
    tovarsh = Column(SmallInteger)
    kodpost = Column(Integer)
    kodfor1c = Column(String(15))
    naclist = Column(SmallInteger)
    skdobl = Column(SmallInteger)
    vedkod = Column(String(20))
    pdv = Column(SmallInteger)
    lastupd = Column(Date)
    rank = Column(SmallInteger)
    checkprice = Column(Numeric(9, 3))
    kodmorion = Column(String(20), index=True)

    grup = relationship('Grup')
    klas = relationship('Klas')


t_name_bbc = Table(
    'name_bbc', metadata,
    Column('kl', String(11)),
    Column('kn', Integer)
)


t_name_darn = Table(
    'name_darn', metadata,
    Column('kl', String(20)),
    Column('kfp', String(20)),
    Column('kn', Integer)
)


t_name_eleg = Table(
    'name_eleg', metadata,
    Column('kl', String(24)),
    Column('kn', Integer)
)


t_name_lk = Table(
    'name_lk', metadata,
    Column('kod', Integer, nullable=False, index=True),
    Column('kodklass', Integer),
    Column('kodgroup', Integer),
    Column('koded', Integer),
    Column('name', String(80)),
    Column('nprice1', Float),
    Column('nprice2', Float),
    Column('nprice3', Float),
    Column('incdoc', String(1)),
    Column('stopnacenka', String(1)),
    Column('kodvida', SmallInteger),
    Column('kodbc', Integer),
    Column('narkotik', String(1)),
    Column('tiptov', Integer),
    Column('tipimport', String(1)),
    Column('minzapas', Float),
    Column('maxzapas', Float),
    Column('tovzapas1', Float),
    Column('tovzapas2', Float),
    Column('nreg', String(15)),
    Column('srokregb', Date),
    Column('srokrege', Date),
    Column('kodmstate', Integer),
    Column('kodplacestore', String(155)),
    Column('shtrihkod', String(15)),
    Column('intername', Integer),
    Column('prikaz251', String(1)),
    Column('lastcena', String(1)),
    Column('olgtovar', String(1)),
    Column('koddoc', Integer),
    Column('netregistr', SmallInteger),
    Column('allstop', SmallInteger),
    Column('checkk', Integer),
    Column('onlyrecept', SmallInteger),
    Column('kodparent', Integer),
    Column('upakovka', Integer),
    Column('analiztorg', SmallInteger),
    Column('notinzav', SmallInteger),
    Column('tovarsh', SmallInteger),
    Column('kodpost', Integer),
    Column('kodfor1c', String(15)),
    Column('naclist', SmallInteger),
    Column('skdobl', SmallInteger),
    Column('vedkod', String(20)),
    Column('pdv', SmallInteger),
    Column('lastupd', Date),
    Column('rank', SmallInteger),
    Column('checkprice', Numeric(9, 3)),
    Column('kodmorion', String(20), index=True)
)


t_nameres = Table(
    'nameres', metadata,
    Column('kod', Integer, nullable=False),
    Column('kodklass', Integer),
    Column('kodgroup', Integer),
    Column('koded', Integer),
    Column('name', String(80)),
    Column('nprice1', Float),
    Column('nprice2', Float),
    Column('nprice3', Float),
    Column('incdoc', String(1)),
    Column('stopnacenka', String(1)),
    Column('kodvida', SmallInteger),
    Column('kodbc', Integer),
    Column('narkotik', String(1)),
    Column('tiptov', Integer),
    Column('tipimport', String(1)),
    Column('minzapas', Float),
    Column('maxzapas', Float),
    Column('tovzapas1', Float),
    Column('tovzapas2', Float),
    Column('nreg', String(15)),
    Column('srokregb', Date),
    Column('srokrege', Date),
    Column('kodmstate', Integer),
    Column('kodplacestore', String(155)),
    Column('shtrihkod', String(15)),
    Column('intername', Integer),
    Column('prikaz251', String(1)),
    Column('lastcena', String(1)),
    Column('olgtovar', String(1)),
    Column('koddoc', Integer),
    Column('netregistr', SmallInteger),
    Column('allstop', SmallInteger),
    Column('checkk', Integer),
    Column('onlyrecept', SmallInteger),
    Column('kodparent', Integer),
    Column('upakovka', Integer),
    Column('analiztorg', SmallInteger),
    Column('notinzav', SmallInteger),
    Column('tovarsh', SmallInteger),
    Column('kodpost', Integer),
    Column('kodfor1c', String(15)),
    Column('naclist', SmallInteger),
    Column('skdobl', SmallInteger),
    Column('vedkod', String(20)),
    Column('pdv', SmallInteger),
    Column('lastupd', Date),
    Column('rank', SmallInteger),
    Column('checkprice', Numeric(9, 3)),
    Column('kodmorion', String(20), index=True)
)


class Noreplace(db.Model):
    __tablename__ = 'noreplace'

    kodmstate = Column(Integer, primary_key=True, nullable=False)
    kodnorep = Column(Integer, primary_key=True, nullable=False)
    phiz = Column(SmallInteger)
    him = Column(SmallInteger)
    pharm = Column(SmallInteger)


t_nost = Table(
    'nost', metadata,
    Column('schet', Text(3)),
    Column('subschet', Text(3)),
    Column('summak', Float),
    Column('summad', Float),
    Column('nomkv', SmallInteger),
    Column('god', Integer)
)


t_oborot = Table(
    'oborot', metadata,
    Column('kodmat', String(15)),
    Column('tipdoc', SmallInteger),
    Column('datadoc', Date),
    Column('kolvo', Numeric(15, 3)),
    Column('mm', Numeric(scale=0))
)


t_opl = Table(
    'opl', metadata,
    Column('kodkross', Integer),
    Column('dateopl', Date),
    Column('sumopl', Float),
    Column('kodprov', Integer)
)


t_opt_name = Table(
    'opt_name', metadata,
    Column('kl', String(7)),
    Column('kfp', Integer),
    Column('kn', Integer)
)


t_optima = Table(
    'optima', metadata,
    Column('kl', String(20)),
    Column('kfp', String(20)),
    Column('kn', Integer)
)


t_ost = Table(
    'ost', metadata,
    Column('kodskl', Integer),
    Column('mesac', SmallInteger),
    Column('god', Integer),
    Column('kodmat', Text(15)),
    Column('nalik', Float),
    Column('hardresrv', Float),
    Column('summaroz', Float)
)


t_ostatki = Table(
    'ostatki', metadata,
    Column('kodskl', Integer),
    Column('kodmat', String(15), index=True),
    Column('nalik', Float),
    Column('hardreserv', Float),
    Column('summaroz', Float),
    Column('god', Integer),
    Column('mesac', SmallInteger),
    Index('ostatki_idx1', 'kodskl', 'kodmat')
)


class Ostfil(db.Model):
    __tablename__ = 'ostfil'

    kod = Column(Integer, primary_key=True, nullable=False)
    dateost = Column(Date, primary_key=True, nullable=False)
    sumsklost = Column(Numeric(15, 2))
    sumrozost = Column(Numeric(15, 2))


t_ostkassa = Table(
    'ostkassa', metadata,
    Column('kod', Integer),
    Column('god', Integer),
    Column('k1', Float),
    Column('k2', Float),
    Column('k3', Float),
    Column('k4', Float)
)


t_ostpart = Table(
    'ostpart', metadata,
    Column('partner', Integer, nullable=False),
    Column('dateost', Date),
    Column('sumdebet', Float),
    Column('sumkredit', Float)
)


class Perecenskl(db.Model):
    __tablename__ = 'perecenskl'

    nomer = Column(Integer, primary_key=True, nullable=False)
    kodskl = Column(Integer, primary_key=True, nullable=False)
    sumprix = Column(Numeric(15, 2))
    sum3 = Column(Numeric(15, 2))
    kolvo = Column(Numeric(15, 3))
    kodmat = Column(String(15), primary_key=True, nullable=False)
    namekod = Column(Integer)


t_pereocenka = Table(
    'pereocenka', metadata,
    Column('nomer', Integer),
    Column('kodtovara', String(15)),
    Column('oldroz', Numeric(15, 2)),
    Column('newroz', Numeric(15, 2)),
    Column('nametovara', String(80)),
    Column('seria', String(30)),
    Column('ok', String(1)),
    Column('oldprix', Float),
    Column('newprix', Float),
    Column('kolvo', Numeric(15, 3)),
    Index('pereocenka0', 'nomer', 'kodtovara', unique=True)
)


class Peresort(db.Model):
    __tablename__ = 'peresort'

    id = Column(Integer, primary_key=True)
    kod = Column(String(15))
    name = Column(String(40))
    cena = Column(Float)
    summa = Column(Float)
    seria = Column(String(30))
    kolvo = Column(Float)
    kodact = Column(Integer)
    dateact = Column(Date)
    kodskl = Column(Integer)


t_plansch = Table(
    'plansch', metadata,
    Column('kod', Integer),
    Column('name', Text(37)),
    Column('schet', Text(3)),
    Column('subschet', Text(3)),
    Column('parentlevel', SmallInteger),
    Column('mylevel', SmallInteger),
    Column('subkonto', Integer),
    Column('debet', Float),
    Column('kredit', Float),
    Index('scheta', 'parentlevel', 'schet', 'subschet'),
    Index('scheti', 'schet', 'subschet')
)


class Planzak(db.Model):
    __tablename__ = 'planzak'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    proz = Column(String(80))
    kolvo = Column(Float)
    cenaprice = Column(Float)
    idpartner = Column(Integer)
    idprice = Column(Integer)
    idstro = Column(Integer)
    idzav = Column(Integer)
    idname = Column(Integer)
    shapkaplan_id = Column(ForeignKey('shapkaplan.id'))
    kodinprice = Column(String(25))

    shapkaplan = relationship('Shapkaplan')


class Plstore(db.Model):
    __tablename__ = 'plstore'

    kod = Column(Integer, primary_key=True)
    idname = Column(Integer)
    idplace = Column(Integer)


t_polis = Table(
    'polis', metadata,
    Column('kod', Integer, unique=True),
    Column('nomer', String(10)),
    Column('datepolis', Date),
    Column('fam', String(40)),
    Column('summa', Float),
    Column('ostatok', Float),
    Column('comp', Integer)
)


class Postavka(db.Model):
    __tablename__ = 'postavka'

    kod = Column(Integer, primary_key=True)
    name = Column(String(40))
    city = Column(String(30))
    adres = Column(String(255))
    rschet = Column(String(14))
    rschet_chek = Column(String(14))
    mfo = Column(String(10))
    bank = Column(Integer)
    nomnds = Column(String(15))
    nomind = Column(String(12))
    okpo = Column(String(10))
    prim = Column(Text)
    tippost = Column(String(1))
    tippol = Column(String(1))
    adr_sklada = Column(String(30))
    usl_work = Column(String(20))
    mol = Column(String(1))
    daypay = Column(SmallInteger)
    tipsob = Column(String(7))
    postzip = Column(String(6))
    phone1 = Column(String(15))
    phone2 = Column(String(15))
    phone3 = Column(String(15))
    fam1 = Column(String(50))
    fam2 = Column(String(50))
    fam3 = Column(String(50))
    dolg1 = Column(String(10))
    dolg2 = Column(String(10))
    dolg3 = Column(String(10))
    datecreat = Column(Date)
    datelastiz = Column(Date)
    pr1 = Column(String(1))
    pr2 = Column(String(1))
    pr3 = Column(String(1))
    skidka = Column(SmallInteger)
    debet = Column(Float)
    kredit = Column(Float)
    kodplat = Column(Integer)
    adrsklada = Column(String(30))
    uslwork = Column(String(20))
    rschetchek = Column(String(14))
    tipusl = Column(String(1))
    nlic = Column(String(15))
    email = Column(String(40))
    cat = Column(Integer)
    namefull = Column(String(300))
    gran1 = Column(Float)
    gran2 = Column(Float)
    gran3 = Column(Float)
    skd1 = Column(Float)
    skd2 = Column(Float)
    skd3 = Column(Float)
    skdwork = Column(SmallInteger)
    dog_date = Column(Date)
    dog_nomer = Column(String(30))
    dog_active = Column(SmallInteger)
    proctov = Column(Integer)
    proctovnds = Column(Integer)
    proctovotch = Column(SmallInteger)
    proctovndsotch = Column(SmallInteger)
    neplatnds = Column(SmallInteger)


t_postavka_dop = Table(
    'postavka_dop', metadata,
    Column('kod', Integer, nullable=False),
    Column('name', String(40)),
    Column('city', String(30)),
    Column('adres', String(30)),
    Column('rschet', String(14)),
    Column('rschet_chek', String(14)),
    Column('mfo', String(10)),
    Column('bank', Integer),
    Column('nomnds', String(15)),
    Column('nomind', String(12)),
    Column('okpo', String(10)),
    Column('prim', Text),
    Column('tippost', String(1)),
    Column('tippol', String(1)),
    Column('adr_sklada', String(30)),
    Column('usl_work', String(20)),
    Column('mol', String(1)),
    Column('daypay', SmallInteger),
    Column('tipsob', String(7)),
    Column('postzip', String(6)),
    Column('phone1', String(15)),
    Column('phone2', String(15)),
    Column('phone3', String(15)),
    Column('fam1', String(50)),
    Column('fam2', String(50)),
    Column('fam3', String(50)),
    Column('dolg1', String(10)),
    Column('dolg2', String(10)),
    Column('dolg3', String(10)),
    Column('datecreat', Date),
    Column('datelastiz', Date),
    Column('pr1', String(1)),
    Column('pr2', String(1)),
    Column('pr3', String(1)),
    Column('skidka', SmallInteger),
    Column('debet', Float),
    Column('kredit', Float),
    Column('kodplat', Integer),
    Column('adrsklada', String(30)),
    Column('uslwork', String(20)),
    Column('rschetchek', String(14)),
    Column('tipusl', String(1)),
    Column('nlic', String(15)),
    Column('email', String(40)),
    Column('cat', Integer)
)


t_predschet = Table(
    'predschet', metadata,
    Column('id', Integer),
    Column('platel', Integer),
    Column('nomer', String(15)),
    Column('datedoc', Date),
    Column('dateplat', Date),
    Column('cutname', String(40)),
    Column('place', String(40)),
    Column('elplace', String(40)),
    Column('summa', Float),
    Column('summaopl', Float),
    Column('naklad', Integer)
)


t_pricefil = Table(
    'pricefil', metadata,
    Column('kod', Integer, unique=True),
    Column('kodfilia', Integer),
    Column('kodname', Integer),
    Column('price', Float),
    Index('filnam', 'kodfilia', 'kodname')
)


class Pricerank(db.Model):
    __tablename__ = 'pricerank'

    id = Column(Integer, primary_key=True)
    rank = Column(SmallInteger)
    price = Column(Float)


class Pricestro(db.Model):
    __tablename__ = 'pricestro'

    idprice = Column(Integer, primary_key=True)
    idstro = Column(Integer)
    name = Column(String(80))
    proz = Column(String(80))
    kodinprice = Column(String(25))
    pricetam = Column(Float)
    pricework = Column(Float)
    pricedop1 = Column(Float)
    pricedop2 = Column(Float)
    pricedop3 = Column(Float)
    srokbefor = Column(Text(10))
    upakovka = Column(String(10))
    kolvo = Column(Float)
    listprice_id = Column(ForeignKey('listprice.id'), nullable=False)
    dopinfo = Column(String(50))

    listprice = relationship('Listprice')


class Pricezakaz(db.Model):
    __tablename__ = 'pricezakaz'

    id = Column(Integer, primary_key=True)
    idpartner = Column(Integer)
    idplan = Column(Integer)
    idzakaz = Column(Integer)
    datezakaz = Column(Date)
    kolvo = Column(Float)
    cena = Column(Float)
    snd = Column(SmallInteger)
    idname = Column(Integer)
    name = Column(String(60))
    proz = Column(String(60))
    kodinprice = Column(String(25))


t_pripys = Table(
    'pripys', metadata,
    Column('id', Integer, unique=True),
    Column('kodname', Integer),
    Column('seria', String(30)),
    Column('datedoc', Date),
    Column('nomer', String(25)),
    Column('prim', String(150))
)


class Prov(db.Model):
    __tablename__ = 'prov'

    kod = Column(Integer, primary_key=True)
    soderg = Column(Text(40))
    debet = Column(Text(3))
    subdebet = Column(Text(3))
    kredit = Column(Text(3))
    subkredit = Column(Text(3))
    dateop = Column(Date)
    subkd = Column(Integer)
    subkk = Column(Integer)
    summa = Column(Float)
    nomgur = Column(SmallInteger)
    kolvo = Column(Float)
    cena = Column(Float)
    part_pr = Column(Text(1))
    subkdgl = Column(Integer)
    subkkgl = Column(Integer)
    kroskod = Column(Integer)
    tipmod = Column(SmallInteger)
    speckod = Column(Integer)
    tipop = Column(Integer)
    nomnak = Column(Integer, index=True)
    nomsch = Column(Integer)
    nomdog = Column(Integer)
    datenak = Column(Date)
    nomerpp = Column(Text(10))
    dodatok = Column(Text(40))


class Rastvor(db.Model):
    __tablename__ = 'rastvor'

    kod = Column(Integer, primary_key=True)
    name = Column(String(30))


class Reccount(db.Model):
    __tablename__ = 'reccount'

    kod = Column(Integer, primary_key=True)
    kodrec = Column(Integer)
    kodname = Column(Integer)
    quntity = Column(Float)


t_recept = Table(
    'recept', metadata,
    Column('kod', Integer, unique=True),
    Column('name', String(30)),
    Column('chek', String(1))
)


class Rectow(db.Model):
    __tablename__ = 'rectow'

    kod = Column(Integer, primary_key=True)
    name = Column(String(40))
    tipr = Column(String(10))
    kodname = Column(Integer)
    datecreate = Column(Date)
    datelastmake = Column(Date)
    makekolvo = Column(Integer)
    place = Column(Integer)
    tarif = Column(Float)
    trudoem = Column(Float)


t_res_grup = Table(
    'res_grup', metadata,
    Column('kod', Integer, nullable=False),
    Column('name', String(30)),
    Column('shortname', String(6)),
    Column('kod_in_klass', Integer),
    Column('kassakod', Integer)
)


t_res_klass = Table(
    'res_klass', metadata,
    Column('kod', Integer, nullable=False),
    Column('name', String(30)),
    Column('country', String(20)),
    Column('skidka', Float),
    Column('holder', Integer)
)


t_res_name = Table(
    'res_name', metadata,
    Column('kod', Integer, nullable=False),
    Column('kodklass', Integer),
    Column('kodgroup', Integer),
    Column('koded', Integer),
    Column('name', String(40)),
    Column('nprice1', Float),
    Column('nprice2', Float),
    Column('nprice3', Float),
    Column('incdoc', String(1)),
    Column('stopnacenka', String(1)),
    Column('kodvida', SmallInteger),
    Column('kodbc', Integer),
    Column('narkotik', String(1)),
    Column('tiptov', Integer),
    Column('tipimport', String(1)),
    Column('minzapas', Float),
    Column('maxzapas', Float),
    Column('tovzapas1', Float),
    Column('tovzapas2', Float),
    Column('nreg', String(15)),
    Column('srokregb', Date),
    Column('srokrege', Date),
    Column('kodmstate', Integer),
    Column('kodplacestore', String(155)),
    Column('shtrihkod', String(15)),
    Column('intername', Integer),
    Column('prikaz251', String(1)),
    Column('lastcena', String(1)),
    Column('olgtovar', String(1)),
    Column('koddoc', Integer),
    Column('netregistr', SmallInteger),
    Column('allstop', SmallInteger),
    Column('checkk', Integer),
    Column('onlyrecept', SmallInteger),
    Column('kodparent', Integer),
    Column('upakovka', Integer),
    Column('analiztorg', SmallInteger),
    Column('notinzav', SmallInteger),
    Column('tovarsh', SmallInteger),
    Column('kodpost', Integer),
    Column('kodfor1c', String(15)),
    Column('naclist', SmallInteger),
    Column('skdobl', SmallInteger)
)


class Rschet(db.Model):
    __tablename__ = 'rschet'

    kod = Column(Integer, primary_key=True)
    name = Column(Text(30))
    summa = Column(Numeric(15, 2))
    kodbank = Column(Integer)
    nomscheta = Column(Text(14))
    valuta = Column(Text(4))
    closedoc = Column(Integer)


t_salefap = Table(
    'salefap', metadata,
    Column('krossnom', Numeric(scale=0)),
    Column('nomer', String(15)),
    Column('sumcom', Float),
    Column('name', String(30)),
    Column('kod', Numeric(scale=0)),
    Column('datedoc', Date),
    Column('tip', String(20)),
    Column('kodskl', Numeric(scale=0))
)


class Sborka(db.Model):
    __tablename__ = 'sborka'

    kod = Column(Integer, primary_key=True)
    name = Column(String(40))


t_sertif = Table(
    'sertif', metadata,
    Column('kodtovara', String(15), unique=True),
    Column('namefilesertf', String(255)),
    Column('pachka', Integer),
    Column('inpachka', Integer)
)


t_shabxls = Table(
    'shabxls', metadata,
    Column('kod', String(15)),
    Column('cena', Float)
)


class Shapkaplan(db.Model):
    __tablename__ = 'shapkaplan'

    id = Column(Integer, primary_key=True)
    dateintro = Column(Date)
    comment = Column(String(80))


t_skidka = Table(
    'skidka', metadata,
    Column('kod', Integer, nullable=False),
    Column('name', Text(40)),
    Column('skidka', Float)
)


class Skidkashag(db.Model):
    __tablename__ = 'skidkashag'

    kod = Column(Integer, primary_key=True)
    gran1 = Column(Float)
    gran2 = Column(Float)
    skidkacom = Column(Float)
    skidkareg = Column(Float)
    skidnds = Column(Float)
    id = Column(SmallInteger)
    skidprikaz = Column(Float)


class Skidkatime(db.Model):
    __tablename__ = 'skidkatime'

    id = Column(Integer, primary_key=True)
    begtime = Column(Time)
    endtime = Column(Time)
    skidka = Column(Float)


class Skl(db.Model):
    __tablename__ = 'skl'

    kod = Column(Integer, primary_key=True, nullable=False)
    kodmat = Column(String(15), primary_key=True, nullable=False, index=True)
    reservsch = Column(Float)
    usekor = Column(Integer)
    hardreserv = Column(Numeric(15, 3))
    nalik = Column(Numeric(15, 3))
    oldnalik = Column(Float)
    kodname = Column(ForeignKey('name.kod'))
    kolvomake = Column(Float)
    userupd = Column(Integer)
    krossdoc = Column(Integer)

    name = relationship('Name')


t_skl_log = Table(
    'skl_log', metadata,
    Column('kod', Integer),
    Column('kodmat', String(15)),
    Column('reservsch', Float),
    Column('usekor', Integer),
    Column('hardreserv', Numeric(15, 3)),
    Column('nalik', Numeric(15, 3)),
    Column('oldnalik', Float),
    Column('kodname', Integer),
    Column('kolvomake', Numeric(15, 3)),
    Column('dateoper', DateTime),
    Column('tipoper', Text(1)),
    Column('userupd', Integer),
    Column('krossdoc', Integer)
)


t_skl_reserv = Table(
    'skl_reserv', metadata,
    Column('kod', Integer),
    Column('kodmat', String(15)),
    Column('nalik', Numeric(15, 2))
)


t_sklinv = Table(
    'sklinv', metadata,
    Column('kodinv', Integer),
    Column('workplace', SmallInteger),
    Column('kod', Integer),
    Column('kodmat', Text(15)),
    Column('fact', Numeric(15, 3)),
    Column('nalik', Numeric(15, 3)),
    Column('kolvomake', Float),
    Column('kolvofact', Float),
    Column('otpusk', Numeric(15, 3))
)


class Standop(db.Model):
    __tablename__ = 'standop'

    kod = Column(Integer, primary_key=True)
    name = Column(Text(30))
    debet = Column(Text(3))
    subdebet = Column(Text(3))
    kredit = Column(Text(3))
    subkredit = Column(Text(3))
    parentlevel = Column(Integer, index=True)
    formula = Column(Text(50))


class Statusnabor(db.Model):
    __tablename__ = 'statusnabor'

    kod = Column(Integer, primary_key=True)
    name = Column(String(40))
    nabor = Column(Integer)


t_straxcom = Table(
    'straxcom', metadata,
    Column('kod', Integer, unique=True),
    Column('name', String(30)),
    Column('okpo', String(12))
)


class Tabgrancena(db.Model):
    __tablename__ = 'tabgrancena'

    id = Column(Integer, primary_key=True)
    gran1 = Column(Float)
    gran2 = Column(Float)
    torgcen = Column(Float)


class Tabgranproc(db.Model):
    __tablename__ = 'tabgranproc'

    id = Column(Integer, primary_key=True)
    gran1 = Column(Float)
    gran2 = Column(Float)
    torgcen = Column(Float)


t_tabgrantorg = Table(
    'tabgrantorg', metadata,
    Column('id', Integer, nullable=False),
    Column('gran1', Float),
    Column('gran2', Float),
    Column('torgcen', Float),
    Column('torgcennds', Float),
    Column('torgcenotch', Float),
    Column('torgcenndsotch', Float)
)


t_tenderprice = Table(
    'tenderprice', metadata,
    Column('kodname', ForeignKey('name.kod'), nullable=False),
    Column('kodpart', ForeignKey('postavka.kod'), nullable=False),
    Column('cena', Float)
)


t_test = Table(
    'test', metadata,
    Column('kl', String(20)),
    Column('kfp', String(20)),
    Column('kn', Integer)
)


t_test_mmo = Table(
    'test_mmo', metadata,
    Column('kl', String(20)),
    Column('kfp', String(20)),
    Column('kn', Integer)
)


class Tip(db.Model):
    __tablename__ = 'tip'

    kod = Column(Integer, primary_key=True)
    name = Column(String(30))
    tip = Column(SmallInteger)


t_tipprint = Table(
    'tipprint', metadata,
    Column('tip', SmallInteger),
    Column('namefile', String(100)),
    Column('kod', Integer),
    Column('nameshab', String(50))
)


t_tipreleas = Table(
    'tipreleas', metadata,
    Column('kod', Integer, nullable=False),
    Column('name', String(40))
)


t_titlezakaz = Table(
    'titlezakaz', metadata,
    Column('kod', Integer, nullable=False),
    Column('title', String(40)),
    Column('datecreate', Date),
    Column('postavka', Integer),
    Column('sendmail', SmallInteger)
)


t_tmpkm = Table(
    'tmpkm', metadata,
    Column('a', String(10)),
    Column('b', String(60)),
    Column('c', String(40)),
    Column('d', String(8)),
    Column('e', String(10)),
    Column('f', String(10)),
    Column('g', String(10)),
    Column('h', String(10)),
    Column('i', String(13)),
    Column('j', String(12))
)


t_tmplikiu = Table(
    'tmplikiu', metadata,
    Column('a', String(30)),
    Column('b', String(30)),
    Column('c', String(30)),
    Column('d', String(120)),
    Column('e', String(84)),
    Column('f', String(30)),
    Column('g', String(54)),
    Column('h', String(32))
)


class Tovarreserv(db.Model):
    __tablename__ = 'tovarreserv'

    kod = Column(Integer, primary_key=True)
    kodskl = Column(Integer)
    kodmat = Column(String(15))
    kodname = Column(Integer)
    iduser = Column(Integer)
    dateoper = Column(Date)
    dateclose = Column(DateTime)
    prichina = Column(String(150))
    kolvo = Column(Numeric(15, 3))
    schkross = Column(Integer)


t_trans = Table(
    'trans', metadata,
    Column('id', Integer),
    Column('tipf', Text(1)),
    Column('kross', Integer),
    Column('datedoc', Date),
    Column('dbefor', Date),
    Column('tipnds', SmallInteger),
    Column('nomer', Text(15)),
    Column('sumcom', Numeric(15, 2)),
    Column('sumnds', Numeric(15, 2)),
    Column('kodmat', Text(15)),
    Column('seria', Text(30)),
    Column('shtrihkod', Text(15)),
    Column('kolvo', Numeric(15, 3)),
    Column('cenarasx', Numeric(15, 5)),
    Column('cenaprix', Numeric(15, 5)),
    Column('cenatam', Numeric(15, 5)),
    Column('cenaroz', Numeric(15, 5)),
    Column('incnds', Text(1)),
    Column('tipimport', Text(1)),
    Column('kodname', Integer),
    Column('kodklass', Integer),
    Column('kodgroup', Integer),
    Column('kodmstate', Integer),
    Column('koded', Integer),
    Column('kodvida', Integer),
    Column('nname', Text(40)),
    Column('nklass', Text(30)),
    Column('ngroup', Text(30)),
    Column('nmstate', Text(40)),
    Column('nvida', Text(30)),
    Column('ned', Text(4)),
    Column('ncen', Text(40)),
    Column('nreg', Text(15)),
    Column('nomsertf', Text(15)),
    Column('datereg', Date),
    Column('datesertf', Date),
    Column('vedkod', String(20))
)


class Tzdatum(db.Model):
    __tablename__ = 'tzdata'

    kod = Column(Integer, primary_key=True)
    mesac = Column(SmallInteger)
    god = Column(Integer)
    droznica = Column(Numeric(15, 2))
    dzakupka = Column(Numeric(15, 2))
    idsklada = Column(Integer)


t_ucshkala = Table(
    'ucshkala', metadata,
    Column('nmonth', SmallInteger, unique=True),
    Column('procent', Float)
)


t_unishtrih = Table(
    'unishtrih', metadata,
    Column('kod', Numeric(scale=0)),
    Column('shtrihkod', String(15))
)


t_user_params = Table(
    'user_params', metadata,
    Column('idreport', Integer, nullable=False),
    Column('name', String(100)),
    Column('caption', String(200)),
    Column('fieldtype', String(100)),
    Column('valueparam', String(200)),
    Column('fieldtypeint', Integer)
)


class UserReport(db.Model):
    __tablename__ = 'user_report'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    sqltext = Column(Text)
    fr3text = Column(LargeBinary)


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String(50))
    fullname = Column(String(80))
    _pass = Column('pass', String(40))
    lastaccess = Column(DateTime)
    createddate = Column(Date)
    accesscount = Column(Integer)
    group_id = Column(Integer)
    enabled = Column(Integer)
    lastacctime = Column(Time)
    createdtime = Column(Time)
    a = Column(Integer)


t_versia = Table(
    'versia', metadata,
    Column('versia', Float)
)


class Vid(db.Model):
    __tablename__ = 'vid'

    kod = Column(Integer, primary_key=True)
    name = Column(String(40))
    rastvor = Column(String(1))
    doza = Column(String(1))
    steril = Column(String(1))
    speckod = Column(Integer)


t_virtskl = Table(
    'virtskl', metadata,
    Column('kodmat', String(15)),
    Column('nametov', String(80)),
    Column('seria', String(30)),
    Column('ostb_k', Float),
    Column('ostb_s', Float),
    Column('prix_k', Float),
    Column('prix_s', Float),
    Column('rasx_k', Float),
    Column('rasx_s', Float),
    Column('pere_k', Float),
    Column('pere_s', Float),
    Column('oste_k', Float),
    Column('oste_s', Float),
    Column('proz', String(30)),
    Column('oster_k', Float),
    Column('oster_s', Float),
    Column('skl_k', Float),
    Column('skl_s', Float),
    Column('skl_r', Float),
    Column('hand_k', Float),
    Column('hand_s', Float),
    Column('hand_r', Float)
)


t_vvs = Table(
    'vvs', metadata,
    Column('kl', String(7)),
    Column('kfp', Integer),
    Column('kn', Integer)
)


class Vyruchka(db.Model):
    __tablename__ = 'vyruchka'

    id = Column(Integer, primary_key=True)
    kodf = Column(Integer, nullable=False)
    datesum = Column(Date, nullable=False)
    vsego = Column(Numeric(15, 2))
    tipop = Column(SmallInteger)
    ucenka = Column(Float)
    kodpartnera = Column(Integer)
    pdv = Column(Float)
    ndocnds = Column(Integer)
    sumopt = Column(Float)
    okpo = Column(String(10))


t_worktab = Table(
    'worktab', metadata,
    Column('kodplat', Integer),
    Column('namepl', Text(30)),
    Column('bd', Float),
    Column('bk', Float),
    Column('prixod', Float),
    Column('plateg', Float),
    Column('rasxod', Float),
    Column('uslugain', Float),
    Column('uslugaout', Float),
    Column('oplata', Float)
)


t_wstore = Table(
    'wstore', metadata,
    Column('kodsklad', Integer),
    Column('kodmat', String(15)),
    Column('worknalik', Float)
)


t_wt02 = Table(
    'wt02', metadata,
    Column('a', String(6)),
    Column('b', String(97)),
    Column('c', String(12)),
    Column('d', String(11)),
    Column('e', String(13), index=True),
    Column('f', String(12)),
    Column('g', String(14)),
    Column('h', String(38)),
    Column('i', String(9)),
    Column('j', String(8))
)


t_zakaz = Table(
    'zakaz', metadata,
    Column('kod', Integer),
    Column('namekod', Integer),
    Column('zakaz', Float),
    Index('zakaz_idx1', 'kod', 'namekod', unique=True)
)


class Zavprice(db.Model):
    __tablename__ = 'zavprice'

    okpo = Column(String(10), primary_key=True, nullable=False)
    kodmat = Column(String(15), primary_key=True, nullable=False)
    zakaz = Column(Numeric(15, 2))
    inwork = Column(Integer, server_default=text("0"))
    cena = Column(Float)
    treb = Column(SmallInteger)
    spname = Column(SmallInteger)


t_zayvka = Table(
    'zayvka', metadata,
    Column('kod', Integer),
    Column('kodfilia', Integer),
    Column('kodname', Integer),
    Column('kolvo', Float),
    Column('price', Float),
    Column('tip', SmallInteger),
    Column('prioritet', SmallInteger),
    Column('yeskolvo', Float),
    Column('kodpzak', Integer),
    Column('mail', String(1))
)
