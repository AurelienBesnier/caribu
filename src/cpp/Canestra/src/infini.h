#include "verbose.h"

#ifdef _INFINI
#define EXTR
#else
#define EXTR extern
#endif

// protos utilise dans Canopy
#define REELLE float
EXTR void
infinitise(void*** Zprim,
           REELLE** Zbuf,
           double,
           int** roof,
           int Tx,
           int Ty,
           bool dupli);
