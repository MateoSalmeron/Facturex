from mamba import description, context, it, before
from doublex import Spy, when
from expects import expect, equal, raise_error
from doublex_expects import have_been_called, have_been_called_with



with description("Invoice Generator Spec") as self:
    with context("FEATURE: Gnerate invoice"):
        with contxt("Having customer"):
            with context("get customer with info"):
                with it (" customer has name")
                    pass


        # with it("computes port value"):

        #     result = self.external_sip_proxy_service.create(A_NAME, A_HOST, AN_EMPTY_PORT, AN_EMPTY_OPERATOR)

        #     expect(result.port).to(equal(DEFAULT_PORT))

