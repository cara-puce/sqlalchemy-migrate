"""
   `CockroachDB`_ database specific implementations of changeset classes.

   .. _`CockroachDB`: http://www.cockroachlabs.com/
"""
from migrate.changeset import ansisql

import cockroachdb.sqlalchemy.dialect as sa_base
CockroachDBSchemaGenerator = sa_base.DDLCompiler


class CockroachDBColumnGenerator(CockroachDBSchemaGenerator, ansisql.ANSIColumnGenerator):
    """PostgreSQL column generator implementation."""
    pass


class CockroachDBColumnDropper(ansisql.ANSIColumnDropper):
    """PostgreSQL column dropper implementation."""
    pass


class CockroachDBSchemaChanger(ansisql.ANSISchemaChanger):
    """PostgreSQL schema changer implementation."""
    pass


class CockroachDBConstraintGenerator(ansisql.ANSIConstraintGenerator):
    """PostgreSQL constraint generator implementation."""
    pass


class CockroachDBConstraintDropper(ansisql.ANSIConstraintDropper):
    """PostgreSQL constaint dropper implementation."""
    pass


class CockroachDBDialect(ansisql.ANSIDialect):
    columngenerator = CockroachDBColumnGenerator
    columndropper = CockroachDBColumnDropper
    schemachanger = CockroachDBSchemaChanger
    constraintgenerator = CockroachDBConstraintGenerator
    constraintdropper = CockroachDBConstraintDropper
