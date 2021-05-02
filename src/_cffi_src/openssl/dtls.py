INCLUDES = """
#include <openssl/ssl.h>
#include <openssl/bio.h>
typedef STACK_OF(SSL_CIPHER) Cryptography_STACK_OF_SSL_CIPHER;
"""

TYPES = """
static const long DTLS1_VERSION;
static const long DTLS1_2_VERSION;

typedef union bio_addr_st BIO_ADDR;
"""

FUNCTIONS = """
const SSL_METHOD *DTLSv1_2_method(void);
const SSL_METHOD *DTLSv1_2_server_method(void);
const SSL_METHOD *DTLSv1_2_client_method(void);

void SSL_CTX_set_cookie_verify_cb(SSL_CTX *,
                                  int (*) (SSL *,
                                           const unsigned
                                           char *,
                                           unsigned int
                                           ));

int DTLSv1_listen(SSL *, BIO_ADDR *);
"""

CUSTOMIZATIONS = """"""